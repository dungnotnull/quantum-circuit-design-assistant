# INTEGRATION.md — Cross-Skill Integration Guide

## AI-ML Cluster Integration Points

This document describes how the Quantum Circuit Design Assistant integrates with the broader ai-ml cluster of skills.

### 1. Shared Sub-Skill Patterns

#### 1.1 Learner Profiling Pattern

This skill's `sub-profile-intake.md` follows the cluster-standard learner profiling pattern used across multiple ai-ml skills:

- **Compatible with:** Skills 108, 199, 206 (machine learning education skills)
- **Shared dimensions:** Background assessment, goal identification, time budgeting, platform preference
- **Track assignment pattern:** Beginner/Intermediate/Advanced three-tier system
- **Reuse:** The structured intake questions can be adapted for any technical education domain

**Integration pattern:** Other ai-ml skills can invoke this profiling logic when their learners need quantum computing context, and vice versa.

#### 1.2 Concept Module Progression Pattern

The `sub-concept-tutor.md` module structure follows the cluster-standard:

- **Module prerequisites:** Each module explicitly states required prior knowledge
- **Quiz validation:** 70% threshold before advancement
- **Citation requirement:** Every concept cites authoritative sources
- **Track-adaptive depth:** Content depth scales with learner track

**Shared with:** `sub-concept-tutor` from ML algorithm education skills

#### 1.3 Hardware/Tool Selection Advisor Pattern

The `sub-hardware-advisor.md` implements a comparison framework that generalizes to other domains:

- **Scoring rubric:** Quantitative comparison across multiple dimensions
- **Cloud access guidance:** Step-by-step setup for each platform
- **Error mitigation:** Domain-specific optimization strategies
- **Cost estimation:** Budget-conscious recommendations

**Applicable to:** Any skill requiring platform/tool selection (cloud ML services, GPU selection, etc.)

### 2. Knowledge Base Integration

#### 2.1 SECOND-KNOWLEDGE-BRAIN Pattern

The `SECOND-KNOWLEDGE-BRAIN.md` structure is designed for cluster-wide compatibility:

- **Core Concepts section:** Domain fundamentals with citations
- **Research Papers table:** Annotated bibliography with relevance scores
- **Tools & Methods section:** Current state-of-the-art
- **Data Sources section:** Curated list of authoritative sources
- **Update Log:** Automated crawl history

**Reusability:** This pattern can be adapted for any rapidly-evolving technical domain.

#### 2.2 Automated Knowledge Updater

The `tools/knowledge_updater.py` provides a template for domain-specific knowledge crawlers:

- **crawl4ai integration:** Async web crawling with markdown extraction
- **Relevance scoring:** Domain keyword matching
- **Deduplication:** SHA-256 hash-based duplicate detection
- **Scheduled updates:** GitHub Actions or cron integration
- **Graceful degradation:** Fallback parsing methods

**Adaptable for:** Any domain requiring regular literature review (ML papers, security research, etc.)

### 3. Cross-Skill Invocation Pathways

#### 3.1 From Other AI-ML Skills

When a user in another ai-ml skill needs quantum computing context:

```
User (in ML skill): "How would I implement this neural network on quantum hardware?"
→ ML skill invokes /quantum-circuit-design-assistant
→ sub-profile-intake captures quantum-specific background
→ sub-concept-tutor explains quantum machine learning basics
→ sub-circuit-designer sketches a quantum neural network circuit
→ sub-hardware-advisor recommends hardware
→ Returns to ML skill with quantum context
```

#### 3.2 From Quantum Circuit Design Assistant

When a quantum learner needs ML context (e.g., for quantum machine learning):

```
User: "How do I use variational quantum circuits for optimization?"
→ This skill recognizes VQE/QAOA as ML-adjacent
→ Invokes ML education skill for classical optimization background
→ Combines classical ML knowledge with quantum circuit design
→ Produces integrated quantum-classical workflow
```

### 4. Evaluation Framework Compatibility

#### 4.1 Scoring Engine Pattern

While this skill does not implement a formal scoring engine, the hardware comparison rubric follows a compatible pattern:

- **Multi-dimensional scoring:** Qubits, fidelity, connectivity, ecosystem, cost
- **Weighted summation:** Different dimensions prioritized by use case
- **Normalized scores:** 0-5 scale for consistency
- **Justification required:** Scores must cite sources

**Future integration:** Can connect to cluster-level `sub-scoring-engine` for standardized assessment.

#### 4.2 Progress Tracking Pattern

The learner profile and milestone system follow the cluster standard:

- **Prerequisite tracking:** Explicit gap identification
- **Next milestones:** 3 concrete next steps with resources
- **Session scoping:** Realistic goal setting based on time budget
- **Progress preservation:** Profile persists across sessions

### 5. Non-Circular Reference Guarantees

All cross-skill references are designed to avoid circular dependencies:

- **Unidirectional invocation:** Quantum skill can be invoked by ML skills, but does not require ML skills to function
- **Fallback-first design:** If ML skills are unavailable, quantum skill provides standalone quantum ML explanation
- **Independent operation:** All sub-skills work without external skill dependencies
- **API boundary:** Cross-skill communication passes through simple text-based interfaces

### 6. Shared Tool Catalog

Tools used by this skill that may benefit other ai-ml skills:

| Tool | Quantum Use Case | Reusable For |
|------|------------------|--------------|
| WebSearch | Latest hardware specs, Qiskit API docs | Live API docs, recent papers |
| WebFetch | Platform documentation, ArXiv abstracts | Technical documentation |
| Read | SECOND-KNOWLEDGE-BRAIN.md fallback | Any structured knowledge base |
| Bash | knowledge_updater.py cron execution | Scheduled script execution |
| Write | Output document generation | Report generation |

### 7. Integration Testing

To verify cross-skill integration works correctly:

```bash
# Test 1: Direct invocation
/quantum-circuit-design-assistant "I'm a Python dev, teach me quantum"

# Test 2: Cross-skill invocation (from ML skill context)
"Compare quantum circuit optimization with neural network optimization"

# Test 3: Knowledge updater standalone
python tools/knowledge_updater.py --dry-run --source arxiv_quant_ph_recent

# Test 4: GitHub Actions trigger
# Manually trigger workflow from Actions tab with dry_run=true
```

### 8. Future Cluster-Level Enhancements

Potential shared components for future ai-ml cluster standardization:

1. **Standardized learner profile schema** — JSON format portable across skills
2. **Shared citation database** — Common bibliographic references
3. **Unified assessment engine** — Cluster-wide quiz/scoring system
4. **Progress tracking API** — Cross-skill learning path management
5. **Knowledge base merge protocol** — Combine multiple SECOND-KNOWLEDGE-BRAIN files

---

**Last Updated:** 2026-07-01
**Cluster:** ai-ml
**Skill ID:** #245 (quantum-circuit-design-assistant)
