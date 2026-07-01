"""
knowledge_updater.py — Quantum Circuit Design Learning Assistant (Skill #245)

Automated weekly crawl pipeline for SECOND-KNOWLEDGE-BRAIN.md.

Uses crawl4ai to fetch the latest quantum computing research papers and hardware
announcements from ArXiv quant-ph, IBM Quantum, Google Quantum AI, Nature Quantum
Information, Physical Review Letters, IonQ, and Quantinuum.

Deduplicates by SHA-256 hash of DOI or canonical URL.
Appends new entries to SECOND-KNOWLEDGE-BRAIN.md with date stamp.
Logs each update run with count of new items and sources crawled.

Recommended schedule: weekly cron (Sunday 02:00 UTC)
  crontab: 0 2 * * 0 /path/to/venv/bin/python /path/to/knowledge_updater.py

Requirements:
    pip install crawl4ai aiohttp feedparser beautifulsoup4 lxml

Usage:
    python knowledge_updater.py [--dry-run] [--source SOURCE_NAME]

    --dry-run: fetch and parse but do not write to SECOND-KNOWLEDGE-BRAIN.md
    --source: run only the named source (default: all sources)
"""

import asyncio
import argparse
import hashlib
import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import feedparser
    from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"Required package not installed: {e}")
    print("Install with: pip install crawl4ai feedparser beautifulsoup4 lxml")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

KNOWLEDGE_BRAIN_PATH = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
LOG_PATH = Path(__file__).parent / "updater.log"
HASHES_CACHE_PATH = Path(__file__).parent / "seen_hashes.json"

RELEVANCE_THRESHOLD = 0.60
MIN_KEYWORD_MATCHES = 2

QUANTUM_KEYWORDS = [
    "quantum circuit", "quantum computing", "qubit", "quantum gate",
    "quantum error correction", "surface code", "NISQ", "quantum algorithm",
    "superconducting qubit", "trapped ion", "quantum hardware", "Qiskit",
    "quantum volume", "quantum advantage", "quantum supremacy",
    "fault tolerant quantum", "logical qubit", "quantum benchmark",
    "quantum processor", "quantum annealing", "quantum simulation",
    "variational quantum", "VQE", "QAOA", "quantum fourier transform",
    "phase estimation", "Grover", "Shor", "quantum teleportation",
    "entanglement", "Bell state", "quantum decoherence", "coherence time",
    "gate fidelity", "quantum noise", "quantum error", "quantum memory",
    "quantum network", "quantum internet", "quantum cryptography", "BB84",
    "quantum key distribution", "QKD", "quantum repeater",
    "neutral atom", "photonic qubit", "topological qubit", "Majorana",
    "quantum chemistry", "quantum machine learning", "quantum optimization",
    "quantum speedup", "quantum complexity", "BQP", "QMA"
]

CRAWL_SOURCES = [
    {
        "name": "arxiv_quant_ph_recent",
        "display_name": "ArXiv quant-ph (Recent)",
        "url": "https://arxiv.org/list/quant-ph/recent",
        "rss_url": "https://rss.arxiv.org/rss/quant-ph",
        "type": "arxiv_rss",
        "max_items": 50,
        "priority": 1,
    },
    {
        "name": "arxiv_quant_ph_cs_et",
        "display_name": "ArXiv cs.ET (Emerging Technologies — quantum computing papers)",
        "url": "https://arxiv.org/list/cs.ET/recent",
        "rss_url": "https://rss.arxiv.org/rss/cs.ET",
        "type": "arxiv_rss",
        "max_items": 20,
        "priority": 2,
    },
    {
        "name": "ibm_quantum_blog",
        "display_name": "IBM Quantum Blog",
        "url": "https://www.ibm.com/quantum/blog",
        "type": "html_blog",
        "max_items": 10,
        "priority": 2,
    },
    {
        "name": "google_quantum_ai_blog",
        "display_name": "Google Quantum AI Blog",
        "url": "https://quantumai.google/blog",
        "type": "html_blog",
        "max_items": 10,
        "priority": 2,
    },
    {
        "name": "nature_quantum_info",
        "display_name": "Nature Quantum Information (npj Quantum Information)",
        "url": "https://www.nature.com/npjqi/",
        "rss_url": "https://www.nature.com/npjqi.rss",
        "type": "rss",
        "max_items": 20,
        "priority": 1,
    },
    {
        "name": "physical_review_letters",
        "display_name": "Physical Review Letters",
        "url": "https://journals.aps.org/prl/",
        "rss_url": "https://journals.aps.org/prl/feeds/feed.rss",
        "type": "rss",
        "max_items": 15,
        "priority": 2,
    },
    {
        "name": "ionq_news",
        "display_name": "IonQ News",
        "url": "https://ionq.com/news",
        "type": "html_blog",
        "max_items": 5,
        "priority": 3,
    },
    {
        "name": "quantinuum_news",
        "display_name": "Quantinuum News",
        "url": "https://www.quantinuum.com/news",
        "type": "html_blog",
        "max_items": 5,
        "priority": 3,
    },
]


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class KnowledgeEntry:
    """A single knowledge entry to be appended to SECOND-KNOWLEDGE-BRAIN.md."""
    title: str
    authors: str
    venue: str
    doi_or_url: str
    abstract_or_summary: str
    key_finding: str
    date_fetched: str
    relevance_score: float
    source_name: str
    url_hash: str = field(default="")

    def __post_init__(self):
        if not self.url_hash:
            self.url_hash = compute_hash(self.doi_or_url)

    def to_markdown(self) -> str:
        """Format as SECOND-KNOWLEDGE-BRAIN.md append entry."""
        return (
            f"\n### [{self.date_fetched}] {self.title}\n"
            f"- **Authors:** {self.authors}\n"
            f"- **Venue:** {self.venue}\n"
            f"- **DOI/URL:** {self.doi_or_url}\n"
            f"- **Relevance Score:** {self.relevance_score:.2f}\n"
            f"- **Relevance:** {self.abstract_or_summary[:200]}...\n"
            f"- **Key Finding:** {self.key_finding[:300]}\n"
        )


# ---------------------------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------------------------

def compute_hash(identifier: str) -> str:
    """SHA-256 hash of a DOI or URL for deduplication."""
    return hashlib.sha256(identifier.strip().lower().encode()).hexdigest()[:16]


def load_seen_hashes() -> set:
    """Load the set of already-processed entry hashes from cache file."""
    if HASHES_CACHE_PATH.exists():
        try:
            with open(HASHES_CACHE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return set(data.get("hashes", []))
        except (json.JSONDecodeError, KeyError):
            return set()
    return set()


def save_seen_hashes(hashes: set) -> None:
    """Persist the updated set of hashes to cache file."""
    with open(HASHES_CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump({"hashes": list(hashes), "last_updated": datetime.now(timezone.utc).isoformat()}, f, indent=2)


def compute_relevance_score(text: str) -> float:
    """
    Score a text's relevance to quantum computing (0.0-1.0).
    Uses keyword matching with recency bonus and logarithmic normalization.
    """
    text_lower = text.lower()
    matches = sum(1 for kw in QUANTUM_KEYWORDS if kw.lower() in text_lower)
    if matches == 0:
        return 0.0
    # Logarithmic normalization: 5+ matches = 1.0
    import math
    score = min(1.0, math.log(matches + 1) / math.log(6))
    return round(score, 3)


def extract_doi_from_text(text: str) -> Optional[str]:
    """Extract DOI if present in text."""
    doi_pattern = r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+'
    match = re.search(doi_pattern, text)
    if match:
        return f"https://doi.org/{match.group()}"
    return None


def clean_text(text: str) -> str:
    """Remove excessive whitespace and HTML entities."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()


# ---------------------------------------------------------------------------
# Source Parsers
# ---------------------------------------------------------------------------

async def fetch_arxiv_rss(source: dict, crawler: AsyncWebCrawler) -> list[KnowledgeEntry]:
    """
    Fetch and parse ArXiv RSS feed for quantum computing papers.
    Returns list of KnowledgeEntry objects passing the relevance threshold.
    """
    rss_url = source.get("rss_url", source["url"])
    logging.info(f"Fetching ArXiv RSS: {rss_url}")

    try:
        config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        result = await crawler.arun(url=rss_url, config=config)
        raw_content = result.html or result.markdown or ""
    except Exception as e:
        logging.warning(f"crawl4ai failed for {rss_url}: {e}. Falling back to feedparser.")
        raw_content = None

    # Parse with feedparser (handles both live and cached content)
    if raw_content:
        feed = feedparser.parse(raw_content)
    else:
        feed = feedparser.parse(rss_url)

    entries = []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for item in feed.entries[:source.get("max_items", 50)]:
        title = clean_text(getattr(item, "title", "Untitled"))
        summary = clean_text(getattr(item, "summary", ""))
        link = getattr(item, "link", "")
        authors_list = getattr(item, "authors", [])
        authors = ", ".join(a.get("name", "") for a in authors_list) if authors_list else "Unknown Authors"
        if not authors.strip():
            authors = getattr(item, "author", "Unknown Authors")

        # Combine title + summary for relevance scoring
        combined_text = f"{title} {summary}"
        score = compute_relevance_score(combined_text)

        if score < RELEVANCE_THRESHOLD:
            continue

        # Extract ArXiv ID for canonical URL
        arxiv_id_match = re.search(r'arxiv\.org/abs/(\S+)', link)
        doi_or_url = f"https://arxiv.org/abs/{arxiv_id_match.group(1)}" if arxiv_id_match else link

        # Key finding = first 2 sentences of abstract
        sentences = summary.split('. ')
        key_finding = '. '.join(sentences[:2]) + ('.' if len(sentences) > 2 else '')

        entries.append(KnowledgeEntry(
            title=title[:200],
            authors=authors[:200],
            venue="ArXiv quant-ph (preprint)",
            doi_or_url=doi_or_url,
            abstract_or_summary=f"Quantum computing paper — relevance: {score:.2f}. {summary[:200]}",
            key_finding=key_finding[:300],
            date_fetched=today,
            relevance_score=score,
            source_name=source["name"],
        ))

    logging.info(f"  ArXiv {source['name']}: {len(entries)} relevant entries (threshold {RELEVANCE_THRESHOLD})")
    return entries


async def fetch_rss_feed(source: dict, crawler: AsyncWebCrawler) -> list[KnowledgeEntry]:
    """
    Generic RSS feed parser (Nature Quantum Information, Physical Review Letters).
    """
    rss_url = source.get("rss_url", source["url"])
    logging.info(f"Fetching RSS: {rss_url}")

    feed = feedparser.parse(rss_url)
    entries = []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for item in feed.entries[:source.get("max_items", 20)]:
        title = clean_text(getattr(item, "title", "Untitled"))
        summary = clean_text(getattr(item, "summary", ""))
        link = getattr(item, "link", "")
        authors_list = getattr(item, "authors", [])
        authors = ", ".join(a.get("name", "") for a in authors_list) if authors_list else getattr(item, "author", "Unknown Authors")

        combined_text = f"{title} {summary}"
        score = compute_relevance_score(combined_text)

        if score < RELEVANCE_THRESHOLD:
            continue

        doi_candidate = extract_doi_from_text(link + " " + summary)
        doi_or_url = doi_candidate or link

        sentences = summary.split('. ')
        key_finding = '. '.join(sentences[:2]) + '.'

        venue_map = {
            "nature_quantum_info": "Nature Quantum Information (npj Quantum Information)",
            "physical_review_letters": "Physical Review Letters",
        }
        venue = venue_map.get(source["name"], source.get("display_name", "Unknown Venue"))

        entries.append(KnowledgeEntry(
            title=title[:200],
            authors=authors[:200],
            venue=venue,
            doi_or_url=doi_or_url,
            abstract_or_summary=f"Peer-reviewed: {summary[:200]}",
            key_finding=key_finding[:300],
            date_fetched=today,
            relevance_score=score,
            source_name=source["name"],
        ))

    logging.info(f"  RSS {source['name']}: {len(entries)} relevant entries")
    return entries


async def fetch_html_blog(source: dict, crawler: AsyncWebCrawler) -> list[KnowledgeEntry]:
    """
    Crawl an HTML blog page (IBM Quantum, Google Quantum AI, IonQ, Quantinuum).
    Extracts article titles, dates, and links from the listing page.
    Then fetches each article for its content.
    """
    logging.info(f"Fetching blog: {source['url']}")
    entries = []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            word_count_threshold=50,
        )
        result = await crawler.arun(url=source["url"], config=config)
        content = result.markdown or result.cleaned_html or ""
    except Exception as e:
        logging.error(f"Failed to crawl {source['url']}: {e}")
        return []

    # Parse article links from the crawled content
    soup = BeautifulSoup(result.html or "", "html.parser")

    # Common blog listing selectors — try each
    article_links = []
    for selector in ["article a", "h2 a", "h3 a", ".post-title a", ".entry-title a", "a[href*='/blog/'], a[href*='/news/']"]:
        found = soup.select(selector)
        if found:
            article_links.extend(found)

    # Deduplicate and filter
    seen_hrefs = set()
    unique_links = []
    base_domain = re.match(r'https?://[^/]+', source["url"]).group()
    for link in article_links:
        href = link.get("href", "")
        if not href or href in seen_hrefs:
            continue
        if href.startswith("/"):
            href = base_domain + href
        if not href.startswith("http"):
            continue
        seen_hrefs.add(href)
        unique_links.append((link.get_text(strip=True), href))

    # Score each linked article
    for title_text, url in unique_links[:source.get("max_items", 10)]:
        score = compute_relevance_score(title_text)
        if score < RELEVANCE_THRESHOLD:
            continue

        # Fetch article content for key finding
        try:
            article_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, word_count_threshold=100)
            article_result = await crawler.arun(url=url, config=article_config)
            article_content = clean_text(article_result.markdown or article_result.cleaned_html or "")[:500]
        except Exception:
            article_content = title_text

        key_finding = article_content[:300] if article_content else title_text

        entries.append(KnowledgeEntry(
            title=title_text[:200] or "Untitled",
            authors=source.get("display_name", "Unknown").replace(" Blog", "").replace(" News", "") + " Team",
            venue=source.get("display_name", "Industry Blog"),
            doi_or_url=url,
            abstract_or_summary=f"Industry announcement: {article_content[:200]}",
            key_finding=key_finding,
            date_fetched=today,
            relevance_score=score,
            source_name=source["name"],
        ))

    logging.info(f"  Blog {source['name']}: {len(entries)} relevant entries")
    return entries


# ---------------------------------------------------------------------------
# Main Crawl Orchestrator
# ---------------------------------------------------------------------------

async def crawl_all_sources(
    sources: list[dict],
    seen_hashes: set,
    dry_run: bool = False,
    target_source: Optional[str] = None,
) -> tuple[list[KnowledgeEntry], set]:
    """
    Run all crawlers, deduplicate results, and return new entries.

    Returns:
        new_entries: list of KnowledgeEntry objects not seen before
        updated_hashes: updated set of hashes (seen_hashes + new entries)
    """
    all_entries: list[KnowledgeEntry] = []

    async with AsyncWebCrawler() as crawler:
        for source in sources:
            if target_source and source["name"] != target_source:
                continue

            try:
                source_type = source.get("type", "html_blog")
                if source_type == "arxiv_rss":
                    entries = await fetch_arxiv_rss(source, crawler)
                elif source_type == "rss":
                    entries = await fetch_rss_feed(source, crawler)
                elif source_type == "html_blog":
                    entries = await fetch_html_blog(source, crawler)
                else:
                    logging.warning(f"Unknown source type '{source_type}' for {source['name']}")
                    continue

                all_entries.extend(entries)

            except Exception as e:
                logging.error(f"Error processing source {source['name']}: {e}")
                continue

    # Deduplicate against seen hashes
    new_entries = []
    updated_hashes = set(seen_hashes)

    for entry in all_entries:
        if entry.url_hash in updated_hashes:
            logging.debug(f"  SKIP (duplicate): {entry.title[:60]}")
            continue
        updated_hashes.add(entry.url_hash)
        new_entries.append(entry)

    # Sort by relevance score descending
    new_entries.sort(key=lambda e: e.relevance_score, reverse=True)

    logging.info(f"Total new entries (after deduplication): {len(new_entries)}")
    return new_entries, updated_hashes


# ---------------------------------------------------------------------------
# SECOND-KNOWLEDGE-BRAIN.md Updater
# ---------------------------------------------------------------------------

def append_to_knowledge_brain(entries: list[KnowledgeEntry], knowledge_brain_path: Path) -> None:
    """
    Append new entries to SECOND-KNOWLEDGE-BRAIN.md in the Knowledge Update Log section
    and Research Papers table.
    """
    if not entries:
        logging.info("No new entries to append.")
        return

    if not knowledge_brain_path.exists():
        logging.error(f"SECOND-KNOWLEDGE-BRAIN.md not found at {knowledge_brain_path}")
        return

    with open(knowledge_brain_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Separate ArXiv/journal papers from blog posts
    papers = [e for e in entries if e.source_name in ("arxiv_quant_ph_recent", "arxiv_quant_ph_cs_et", "nature_quantum_info", "physical_review_letters")]
    blog_posts = [e for e in entries if e not in papers]

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    n_new = len(entries)
    sources_crawled = list({e.source_name for e in entries})

    # Build update log entry
    log_entry = (
        f"\n### [{today}] Automated Knowledge Update Run\n"
        f"- **New entries added:** {n_new}\n"
        f"- **Sources crawled:** {', '.join(sources_crawled)}\n"
        f"- **Papers:** {len(papers)}, **Blog/News posts:** {len(blog_posts)}\n"
        f"- **Next crawl scheduled:** Weekly (Sunday 02:00 UTC)\n"
    )

    # Append new paper entries as sub-section
    if papers:
        papers_block = "\n## Newly Crawled Research Papers\n"
        for entry in papers:
            papers_block += entry.to_markdown()
    else:
        papers_block = ""

    if blog_posts:
        blog_block = "\n## Newly Crawled Industry Announcements\n"
        for entry in blog_posts:
            blog_block += entry.to_markdown()
    else:
        blog_block = ""

    # Insert before the final line of the file (the "*End of*" line)
    end_marker = "*End of SECOND-KNOWLEDGE-BRAIN.md"
    if end_marker in content:
        insert_before = content.rfind(end_marker)
        updated_content = (
            content[:insert_before]
            + log_entry
            + papers_block
            + blog_block
            + "\n---\n\n"
            + content[insert_before:]
        )
    else:
        # Append at end if marker not found
        updated_content = content + log_entry + papers_block + blog_block

    with open(knowledge_brain_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    logging.info(f"Appended {n_new} new entries to {knowledge_brain_path}")


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with latest quantum computing research"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and parse but do not write to SECOND-KNOWLEDGE-BRAIN.md",
    )
    parser.add_argument(
        "--source",
        type=str,
        default=None,
        help="Run only this named source (e.g. arxiv_quant_ph_recent)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable DEBUG logging",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_PATH, encoding="utf-8"),
        ],
    )

    logging.info("=" * 60)
    logging.info("Quantum Circuit Design Assistant — Knowledge Updater")
    logging.info(f"Run started: {datetime.now(timezone.utc).isoformat()}")
    logging.info(f"Dry run: {args.dry_run}")
    logging.info(f"Target source: {args.source or 'ALL'}")
    logging.info(f"Knowledge brain path: {KNOWLEDGE_BRAIN_PATH}")
    logging.info("=" * 60)

    # Load seen hashes for deduplication
    seen_hashes = load_seen_hashes()
    logging.info(f"Loaded {len(seen_hashes)} previously seen entry hashes")

    # Crawl all sources
    new_entries, updated_hashes = await crawl_all_sources(
        sources=CRAWL_SOURCES,
        seen_hashes=seen_hashes,
        dry_run=args.dry_run,
        target_source=args.source,
    )

    if args.dry_run:
        logging.info(f"[DRY RUN] Would have appended {len(new_entries)} new entries.")
        for entry in new_entries[:10]:
            logging.info(f"  [{entry.relevance_score:.2f}] {entry.title[:80]}")
        logging.info("[DRY RUN] No files written.")
        return

    if not new_entries:
        logging.info("No new entries found. SECOND-KNOWLEDGE-BRAIN.md unchanged.")
        # Still save hashes to mark this run
        save_seen_hashes(updated_hashes)
        return

    # Write to SECOND-KNOWLEDGE-BRAIN.md
    append_to_knowledge_brain(new_entries, KNOWLEDGE_BRAIN_PATH)

    # Save updated hash cache
    save_seen_hashes(updated_hashes)

    logging.info(f"Update complete. {len(new_entries)} new entries added.")
    logging.info("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
