# CLAUDE.md — Skill #245: Quantum Circuit Design Learning Assistant

## Skill Identity

- **Skill Name:** quantum-circuit-design-assistant
- **Tagline:** Teach beginners to understand, design, and simulate quantum circuits grounded in authoritative quantum computing curricula
- **Source Idea:** #245
- **Cluster:** ai-ml
- **Current Phase:** ALL PHASES COMPLETE (0-5) — Production-ready, open-source ready

## Problem This Skill Solves

Quantum computing is one of the most technically demanding fields in modern science, yet the educational gap between classical computing expertise and practical quantum circuit design is vast. Beginners face a steep learning curve: abstract mathematical formalism (linear algebra over complex Hilbert spaces), unfamiliar hardware constraints (coherence times, gate fidelity), and rapidly evolving hardware platforms (IBM, Google, IonQ, Quantinuum) each with different gate sets and connectivity topologies.

This skill bridges that gap by acting as a structured, expert-level learning assistant that meets the user at their current level (physics/CS/math background), teaches quantum computing concepts progressively using world-class curricula (Nielsen & Chuang, IBM Quantum Learning, Qiskit Textbook, Preskill lecture notes), helps them design and analyze real quantum circuits (with ASCII diagrams and Qiskit code), advises on hardware platform selection, and continuously updates its knowledge base from ArXiv quant-ph and leading quantum lab publications.

## Harness Flow Summary

```
/quantum-circuit-design-assistant invoked
  Step 1 → sub-profile-intake: Assess user background, goals, and preferred platform
  Step 2 → sub-concept-tutor: Teach required concepts (Bloch sphere, gates, entanglement, algorithms)
  Step 3 → sub-circuit-designer: Design circuit from algorithm description; produce ASCII diagram + Qiskit code
  Step 4 → sub-hardware-advisor: Recommend hardware platform; explain noise, fidelity, connectivity constraints
  Step 5 → Main harness: Synthesize full learning plan + circuit design deliverable with next steps
```

## Sub-Skills List

| File | Description |
|------|-------------|
| `skills/sub-profile-intake.md` | Collects user background (physics/CS/math level), learning goal, preferred hardware platform, and time budget |
| `skills/sub-concept-tutor.md` | Teaches quantum computing concepts progressively; uses worked examples, Bloch sphere descriptions, quizzes |
| `skills/sub-circuit-designer.md` | Translates algorithm descriptions to gate sequences; draws ASCII circuit diagrams; writes Qiskit/Cirq code; analyzes depth and gate count |
| `skills/sub-hardware-advisor.md` | Compares IBM/Google/IonQ/Quantinuum platforms; explains noise characteristics, gate sets, connectivity; guides cloud access |

## Tools Required

- WebSearch — search ArXiv quant-ph, IBM Quantum news, Google Quantum AI blog, Nature Quantum Information
- WebFetch — fetch latest papers, documentation, and lab announcements
- Read — read SECOND-KNOWLEDGE-BRAIN.md for fallback knowledge
- Write — write circuit files, learning plans, and knowledge base updates
- Bash — run knowledge_updater.py; optionally test Qiskit code snippets

## Knowledge Sources

| Source | Category | URL / ArXiv Category |
|--------|----------|----------------------|
| ArXiv quant-ph | Primary research | https://arxiv.org/list/quant-ph/recent |
| Nielsen & Chuang | Textbook | ISBN 978-1107002173 (Cambridge) |
| IBM Quantum Learning | Official curriculum | https://learning.quantum.ibm.com |
| Qiskit Textbook | Open source | https://qiskit.org/learn |
| Google Quantum AI Blog | Lab announcements | https://quantumai.google/blog |
| Nature Quantum Information | Peer-reviewed | https://www.nature.com/npjqi/ |
| Physical Review Letters (quantum) | Peer-reviewed | https://journals.aps.org/prl/ |
| Preskill Lecture Notes | Caltech | http://theory.caltech.edu/~preskill/ph229/ |
| Quantinuum News | Lab announcements | https://www.quantinuum.com/news |
| IonQ Blog | Lab announcements | https://ionq.com/news |

## Supporting Python Tools

- `tools/knowledge_updater.py` — crawl4ai pipeline that fetches from ArXiv quant-ph, IBM Quantum news, Google Quantum AI, Nature Quantum Information; parses title/authors/date/DOI/abstract; appends to SECOND-KNOWLEDGE-BRAIN.md; deduplicates by URL/DOI hash
- **Automation:** GitHub Actions workflow (`.github/workflows/knowledge-updater.yml`) — Weekly scheduled execution every Sunday 02:00 UTC

## Phase Completion Status

✅ **Phase 0: Research & Architecture** — COMPLETE (2026-06-19)
✅ **Phase 1: Core Sub-Skills Implementation** — COMPLETE (2026-06-19)
✅ **Phase 2: Main Harness + Quality Gates** — COMPLETE (2026-06-19)
✅ **Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline** — COMPLETE (2026-06-19)
✅ **Phase 4: Testing & Validation** — COMPLETE (2026-06-19)
✅ **Phase 5: Integration & Cross-Skill Wiring** — COMPLETE (2026-07-01)

**Project Status:** PRODUCTION-GRADE, OPEN-SOURCE READY

## AI-ML Cluster Integration

### Cross-Skill Integration Points

This skill follows ai-ml cluster patterns and integrates with other skills through:

1. **Learner Profiling Pattern** — `sub-profile-intake.md` implements cluster-standard structured intake compatible with skills 108, 199, 206 (ML education)
2. **Concept Module Progression** — `sub-concept-tutor.md` follows cluster-standard module structure with prerequisite tracking, 70% quiz threshold, and track-adaptive depth
3. **Hardware/Tool Selection Advisor** — `sub-hardware-advisor.md` implements a comparison framework generalizable to platform selection in any technical domain
4. **Knowledge Base Pattern** — `SECOND-KNOWLEDGE-BRAIN.md` structure designed for cluster-wide compatibility with core concepts, research papers table, tools/methods, and update log

### Shared Sub-Skill Compatibility

| Sub-Skill Pattern | Quantum Implementation | Reusable For |
|-------------------|------------------------|--------------|
| Learner profiling | 5-dimension intake → 3-track assignment | Any technical education skill |
| Concept modules | 7 modules with prerequisite chains | Progressive learning systems |
| Hardware advisor | Multi-platform scoring rubric | Tool/platform selection skills |
| Knowledge updater | crawl4ai pipeline with deduplication | Literature review automation |

### Non-Circular Reference Guarantees

- Unidirectional invocation: Quantum skill can be invoked by ML skills but doesn't require them
- Fallback-first design: All sub-skills work independently without external dependencies
- API boundary: Cross-skill communication via simple text-based interfaces

### Integration Documentation

See `docs/INTEGRATION.md` for complete cross-skill integration guide, invocation pathways, and future cluster-level enhancements.

## Deployment Checklist

✅ All sub-skills implemented with quality gates
✅ Main harness with 5-step workflow
✅ SECOND-KNOWLEDGE-BRAIN.md populated with 19 research papers
✅ knowledge_updater.py production-ready with crawl4ai
✅ GitHub Actions workflow for weekly automated updates
✅ 6 test scenarios covering Beginner/Intermediate/Advanced tracks
✅ Integration documentation (docs/INTEGRATION.md)
✅ All phases marked complete in PROJECT-DEVELOPMENT-PHASE-TRACKING.md

## Reference Documents

- `PROJECT-detail.md` — Full technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Phase-by-phase build roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — Self-improving domain knowledge base
