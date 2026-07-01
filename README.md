# Quantum Circuit Design Learning Assistant

**Skill #245** — Production-grade, open-source quantum computing education skill

[![Phase Status](https://img.shields.io/badge/Phase-0%2C1%2C2%2C3%2C4%2C5%20COMPLETE-success)](./PROJECT-DEVELOPMENT-PHASE-TRACKING.md)
[![Skills](https://img.shields.io/badge/Cluster-ai--ml-blue)](./CLAUDE.md)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

## Overview

The Quantum Circuit Design Learning Assistant is a structured, expert-level Claude skill that guides beginners through the full arc of quantum computing education — from foundational qubit theory to practical circuit design using Qiskit — grounded in world-class curricula (Nielsen & Chuang, Preskill, IBM Quantum Learning) and continuously updated with the latest hardware advances.

### Key Features

- **Adaptive Learning Paths:** Three tracks (Beginner/Intermediate/Advanced) tailored to user background
- **Circuit Design:** ASCII circuit diagrams + runnable Qiskit code
- **Hardware Advisory:** Platform comparisons with technical specifications
- **Self-Improving Knowledge Base:** Automated weekly updates from ArXiv and leading quantum labs
- **Production-Grade:** 100% complete, all quality gates implemented, open-source ready

## Quick Start

```
/quantum-circuit-design-assistant
```

**Example:**
> "I'm a Python developer with no physics background. Teach me quantum computing and show me the simplest quantum circuit."

The skill will:
1. Assess your background and assign a learning track
2. Teach foundational concepts (qubits, superposition, gates)
3. Design a Bell state circuit with ASCII diagram
4. Provide runnable Qiskit code
5. Recommend the best hardware platform for your goals

## Architecture

```
User invokes /quantum-circuit-design-assistant
  │
  ├─ Step 1: sub-profile-intake (background, goal, platform, time budget)
  ├─ Step 2: sub-concept-tutor (concept modules with quizzes)
  ├─ Step 3: sub-circuit-designer (ASCII diagrams + Qiskit code)
  ├─ Step 4: sub-hardware-advisor (platform comparison)
  └─ Step 5: Main harness (synthesize deliverable)
```

## Sub-Skills

| Sub-Skill | Purpose |
|-----------|---------|
| `sub-profile-intake.md` | Learner profiling and track assignment |
| `sub-concept-tutor.md` | Concept teaching with 7 modules |
| `sub-circuit-designer.md` | Circuit design with ASCII diagrams |
| `sub-hardware-advisor.md` | Hardware platform recommendations |

## Knowledge Base

The skill maintains `SECOND-KNOWLEDGE-BRAIN.md` with:
- 19+ foundational research papers
- 8 authoritative data sources
- 5 core quantum computing concepts
- State-of-the-art tools and methods
- Analytical frameworks (Quantum Volume, AQ metric, cross-entropy)

### Automated Knowledge Updates

The `tools/knowledge_updater.py` script runs weekly via GitHub Actions to:
- Crawl ArXiv quant-ph for latest papers
- Fetch hardware announcements from IBM, Google, IonQ, Quantinuum
- Update knowledge base with new findings
- Deduplicate entries and log changes

## Test Scenarios

The skill includes 6 comprehensive test scenarios:
1. **Beginner:** Python developer — Bell state circuit
2. **Intermediate:** Physics undergrad — Grover's algorithm
3. **Intermediate:** ML researcher — 50-qubit hardware selection
4. **Intermediate:** Circuit depth optimization challenge
5. **Advanced:** PhD student — Quantum error correction
6. **Advanced:** Cryptography PhD — Shor's algorithm feasibility

## Documentation

- [Technical Specification](./PROJECT-detail.md) — Full technical specification
- [Phase Tracking](./PROJECT-DEVELOPMENT-PHASE-TRACKING.md) — Development roadmap
- [Integration Guide](./docs/INTEGRATION.md) — Cross-skill integration
- [Test Scenarios](./tests/test-scenarios.md) — Comprehensive test coverage

## Installation & Setup

### For Development

```bash
# Clone repository
git clone <repository-url>
cd quantum-circuit-design-assistant

# Install dependencies
pip install -r requirements.txt

# Run knowledge updater manually (optional)
python tools/knowledge_updater.py --dry-run

# Run with specific source
python tools/knowledge_updater.py --source arxiv_quant_ph_recent
```

### For Production

The skill is designed for use within Claude Code or compatible AI assistant frameworks. The GitHub Actions workflow handles automated knowledge updates.

## Dependencies

See [requirements.txt](./requirements.txt):
- `crawl4ai` — Web crawling for knowledge updates
- `feedparser` — RSS feed parsing
- `beautifulsoup4` — HTML parsing
- `aiohttp` — Async HTTP requests
- `lxml` — XML/HTML parsing

## AI-ML Cluster Integration

This skill integrates with the broader ai-ml cluster through:

1. **Learner Profiling Pattern** — Compatible with skills 108, 199, 206
2. **Concept Module Progression** — Cluster-standard module structure
3. **Hardware/Tool Selection Advisor** — Generalizable comparison framework
4. **Knowledge Base Pattern** — Adaptable for any technical domain

See [docs/INTEGRATION.md](./docs/INTEGRATION.md) for details.

## Quality Gates

Before any output, the skill verifies:
- ✅ Profile completeness (5 dimensions captured)
- ✅ Citation coverage (all concepts cite sources)
- ✅ Code validity (syntactically correct Qiskit)
- ✅ Hardware accuracy (specs from official sources)
- ✅ Track alignment (content matches learner level)
- ✅ Deliverable completeness (all sections present)
- ✅ Graceful degradation (flags cached knowledge)

## Project Status

**🎉 100% COMPLETE — Production-Ready**

| Phase | Status | Deliverables |
|-------|--------|--------------|
| 0: Research & Architecture | ✅ Complete | CLAUDE.md, PROJECT-detail.md |
| 1: Core Sub-Skills | ✅ Complete | 4 sub-skill files |
| 2: Main Harness | ✅ Complete | skills/main.md |
| 3: Knowledge Brain Pipeline | ✅ Complete | SECOND-KNOWLEDGE-BRAIN.md, knowledge_updater.py |
| 4: Testing & Validation | ✅ Complete | 6 test scenarios |
| 5: Cross-Skill Integration | ✅ Complete | Integration docs, GitHub Actions |

**Total:** 14 files + GitHub Actions workflow (~4,000+ lines)

## License

MIT License — See [LICENSE](./LICENSE) file

## Contributing

This skill is production-ready and prepared for open-source release. Contributions welcome:
- Additional test scenarios
- Platform specification updates
- Circuit optimization techniques
- Integration improvements

## Acknowledgments

Built with authoritative curricula from:
- Nielsen & Chuang, *Quantum Computation and Quantum Information*
- Preskill, Caltech Ph229 Lecture Notes
- IBM Quantum Learning
- Qiskit Textbook
- Leading quantum computing laboratories

---

**Skill ID:** #245
**Cluster:** ai-ml
**Status:** Production-Ready, Open-Source Ready
**Date Completed:** 2026-07-01
