# PROJECT-detail.md — Quantum Circuit Design Learning Assistant (Skill #245)

## Executive Summary

The Quantum Circuit Design Learning Assistant is a structured, expert-level Claude skill that guides beginners through the full arc of quantum computing education — from foundational qubit theory to practical circuit design using Qiskit — grounded in world-class curricula (Nielsen & Chuang, Preskill, IBM Quantum Learning) and continuously updated with the latest hardware advances from leading quantum computing laboratories worldwide. The skill operates as a harness orchestrating four sub-skills covering learner profiling, concept tutoring, circuit design, and hardware advisory, and produces professional-quality deliverables: a personalized learning plan, annotated circuit diagrams (ASCII), working Qiskit code, and a hardware selection recommendation.

---

## Problem Statement

Quantum computing represents one of the most significant technological frontiers of the 21st century, promising exponential speedups for problems in cryptography (Shor's algorithm), search (Grover's algorithm), optimization, and quantum chemistry simulation. However, the educational pathway is exceptionally steep:

1. **Mathematical prerequisites**: Quantum mechanics requires comfort with complex vector spaces, tensor products, unitary matrices, and probability amplitudes — topics not covered in standard CS curricula.
2. **Conceptual novelty**: Superposition, entanglement, and quantum measurement have no classical analogs, making intuition-building uniquely difficult.
3. **Hardware diversity**: Five major hardware paradigms (superconducting, trapped ion, photonic, neutral atom, topological) each impose different gate sets, connectivity constraints, and error profiles.
4. **Rapid evolution**: The field advances monthly — hardware fidelity improvements, new error-correction milestones, and algorithm discoveries constantly shift what is practically achievable.
5. **Tooling fragmentation**: Qiskit, Cirq, PennyLane, Q#, and Braket each have distinct APIs, syntax, and backend support.

Without structured guidance, beginners waste months on the wrong conceptual foundations, write circuits that exceed hardware connectivity limits, or choose platforms poorly suited to their use case. This skill solves all five problems systematically.

**Domain Context:** The quantum computing market is projected to exceed $450 billion by 2040 (McKinsey Global Institute, 2021). IBM has deployed over 100 quantum systems on IBM Quantum Network; Google claimed quantum supremacy with Sycamore (2019, Nature); IonQ achieved 29 algorithmic qubits (2022); Quantinuum demonstrated quantum error correction at scale (2023). The educational gap is a critical bottleneck.

---

## Target Users & Use Cases

### Primary Users
- CS/software engineers with no quantum background who want to enter the field
- Physics undergraduates who understand the theory but need practical circuit design skills
- Math graduates comfortable with linear algebra who want to apply it to quantum computing
- Researchers in adjacent fields (chemistry, optimization, ML) who need quantum algorithm literacy

### Trigger Examples

| User Says | Skill Does |
|-----------|-----------|
| "I'm a Python developer, I want to learn quantum computing from scratch" | Runs full intake, places user at Beginner track, teaches qubit/gates/measurement, designs a Bell state circuit in Qiskit |
| "I understand superposition but I need to design a Grover's algorithm circuit" | Skips basics after intake, goes directly to sub-circuit-designer for Grover's, includes oracle design and diffusion operator |
| "Which quantum computer should I use for a 50-qubit simulation?" | Runs sub-hardware-advisor for large-scale comparison: IBM Eagle vs IonQ Forte vs Quantinuum H2 |
| "Explain entanglement with a code example" | sub-concept-tutor teaches Bell states with Bloch sphere description and Bell circuit in Qiskit |
| "My circuit has depth 200 but I need it under 50 for NISQ hardware" | sub-circuit-designer analyzes gates, proposes transpilation strategies, applies circuit compression |

---

## Harness Architecture

```
                    ┌─────────────────────────────────────────┐
                    │  /quantum-circuit-design-assistant       │
                    │  MAIN HARNESS (skills/main.md)           │
                    └──────────────┬──────────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼                    ▼
  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │ sub-profile-    │  │ sub-concept-     │  │ sub-circuit-     │  │ sub-hardware-    │
  │ intake.md       │  │ tutor.md         │  │ designer.md      │  │ advisor.md       │
  │                 │  │                  │  │                  │  │                  │
  │ Outputs:        │  │ Outputs:         │  │ Outputs:         │  │ Outputs:         │
  │ - User profile  │  │ - Concept briefs │  │ - ASCII circuit  │  │ - Platform score │
  │ - Track level   │  │ - Worked examples│  │ - Qiskit code    │  │ - Noise profile  │
  │ - Goal clarity  │  │ - Quiz results   │  │ - Gate analysis  │  │ - Access guide   │
  │ - Platform pref │  │ - Next concept   │  │ - Optimizations  │  │ - Cost estimate  │
  └────────┬────────┘  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘
           │                    │                      │                      │
           └────────────────────┴──────────────────────┴──────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │  SYNTHESIS & FINAL DELIVERABLE  │
                              │  - Personalized learning plan   │
                              │  - Circuit design document      │
                              │  - Hardware recommendation      │
                              │  - Next 3 learning milestones   │
                              └─────────────────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │  SECOND-KNOWLEDGE-BRAIN.md      │
                              │  (fallback + enrichment)        │
                              │  Updated by knowledge_updater   │
                              └─────────────────────────────────┘
```

---

## Full Sub-Skill Catalog

### 1. sub-profile-intake.md

**Purpose:** Establish the user's starting point and goals before any teaching begins.

**Inputs:**
- User's stated background (physics/CS/math level: none / undergraduate / graduate / professional)
- Learning goal: conceptual understanding, circuit design, research preparation, algorithm implementation
- Time budget: hours per week available
- Preferred hardware or toolchain (IBM/Qiskit, Google/Cirq, IonQ, Microsoft/Q#, agnostic)
- Specific topic or algorithm of interest (optional)

**Outputs:**
- Structured learner profile (JSON-like summary)
- Track assignment: Beginner (no QM background) / Intermediate (knows linear algebra + basic QM) / Advanced (knows QM, wants circuit optimization or hardware-level detail)
- Recommended sub-skill sequence for this session
- Gaps identified (e.g., "needs linear algebra refresher before proceeding")

**Tools Used:** None (conversational intake via structured questions)

**Quality Gate:** Profile must capture all 5 dimensions before proceeding. If user refuses to answer, apply conservative defaults (Beginner track, Qiskit toolchain).

---

### 2. sub-concept-tutor.md

**Purpose:** Teach quantum computing concepts progressively, tailored to the user's track level, using authoritative curricula.

**Inputs:**
- Learner profile from sub-profile-intake
- Target concept(s) to teach in this session
- Track level (Beginner / Intermediate / Advanced)

**Workflow:**
- Select canonical reference (Nielsen & Chuang chapter, Preskill lecture, IBM Learning module)
- Present concept with: (a) intuitive analogy, (b) mathematical formulation, (c) worked example, (d) Qiskit demo code
- Include Bloch sphere visualization (described textually with coordinates for key states)
- Quiz comprehension with 2-3 targeted questions
- Adapt depth based on quiz performance

**Key Concept Modules:**
- Module 1 (Beginner): Qubits and superposition; Dirac notation; Bloch sphere; quantum measurement and Born rule
- Module 2 (Beginner-Intermediate): Single-qubit gates (X, Y, Z, H, S, T, Rx, Ry, Rz); matrix representations; gate composition
- Module 3 (Intermediate): Multi-qubit systems; tensor products; CNOT, Toffoli gates; entanglement; Bell states; GHZ states
- Module 4 (Intermediate): No-cloning theorem; quantum teleportation protocol; dense coding
- Module 5 (Intermediate-Advanced): Quantum algorithms — Deutsch-Jozsa, Bernstein-Vazirani, Grover's search
- Module 6 (Advanced): Shor's factoring algorithm; quantum Fourier transform; phase estimation
- Module 7 (Advanced): Quantum error correction — stabilizer formalism, Steane code, surface codes, logical qubits

**Outputs:**
- Concept brief (structured explanation with all four components)
- Quiz Q&A
- Recommended next concept
- Relevant citation (Nielsen & Chuang section, ArXiv paper, or IBM Learning module)

**Quality Gate:** Every concept explanation must include at least one citation from Nielsen & Chuang or a peer-reviewed source. No claims without evidence.

---

### 3. sub-circuit-designer.md

**Purpose:** Help the user design quantum circuits from algorithm descriptions, producing ASCII diagrams, Qiskit code, and analysis.

**Inputs:**
- Algorithm description or circuit goal (e.g., "create a Bell state", "implement Grover's search for 3 qubits")
- Target hardware platform (for connectivity constraint application)
- Optimization goal: minimize depth, minimize gate count, or minimize CNOT count

**Workflow:**
1. Decompose algorithm into gate sequence
2. Draw ASCII circuit diagram
3. Write complete Qiskit code (with imports, circuit construction, measurement, and simulation)
4. Analyze: circuit depth, gate count by type, estimated T-gate count (for fault-tolerant cost)
5. Identify hardware connectivity issues (if platform specified)
6. Suggest optimizations: gate cancellation, commutation rules, CNOT decomposition
7. Provide transpilation notes for target backend

**ASCII Circuit Format:**
```
q0: ─[H]─────────■─────[M]─
                  │
q1: ─────────────X─────[M]─
```

**Outputs:**
- ASCII circuit diagram
- Complete Qiskit code (runnable on IBM Quantum or local Qiskit Aer simulator)
- Circuit metrics table: depth, gate counts, estimated 2-qubit gate count
- Optimization recommendations (ordered by impact)
- Hardware-specific transpilation notes

**Tools Used:** WebSearch (for latest Qiskit API), WebFetch (Qiskit documentation), Read (SECOND-KNOWLEDGE-BRAIN.md)

**Quality Gate:** Qiskit code must be syntactically correct and include measurement. Circuit depth analysis must reference the target hardware's reported coherence time (T2) and gate fidelity.

---

### 4. sub-hardware-advisor.md

**Purpose:** Compare quantum hardware platforms and guide the user to the appropriate backend for their use case.

**Inputs:**
- Learner profile (experience level, use case)
- Circuit specifications (qubit count, required gate types, circuit depth)
- Budget constraints (free tier vs. paid access)
- Goal (learning, research, production, benchmarking)

**Platform Coverage:**

| Platform | Technology | Key Metric | Access |
|----------|-----------|-----------|--------|
| IBM Quantum (Eagle R3, Heron) | Superconducting | Quantum Volume, CLOPS | Free tier + paid |
| Google Sycamore / Willow | Superconducting | Cross-entropy benchmarking | Research partnership |
| IonQ Forte / Aria | Trapped ion | Algorithmic Qubits (AQ) | Cloud (AWS Braket, Azure) |
| Quantinuum H2 | Trapped ion | QCVV fidelity | Subscription |
| Rigetti Ankaa-2 | Superconducting | QV | AWS Braket |
| D-Wave Advantage | Quantum annealing | QUBO/Ising | Cloud |
| PsiQuantum (future) | Photonic | (pre-commercial) | Research only |

**Outputs:**
- Platform comparison table scored against user requirements
- Recommended platform with justification
- Step-by-step cloud access guide for recommended platform
- Error mitigation strategies specific to chosen platform
- Cost estimate for target computation

**Tools Used:** WebSearch (latest hardware specs), WebFetch (platform documentation), Read (SECOND-KNOWLEDGE-BRAIN.md)

**Quality Gate:** All platform specs (gate fidelity, qubit count, coherence times) must be cited from official platform documentation or peer-reviewed benchmarking papers published within 12 months.

---

## Skill File Format Specification

### Frontmatter Schema
```yaml
---
name: quantum-circuit-design-assistant
description: Guide beginners through quantum circuit design using Nielsen & Chuang curricula, Qiskit code, and live hardware recommendations
---
```

### Required Sections in main.md
1. Role & Persona
2. Workflow (numbered harness flow, 5 steps)
3. Sub-skills Available (table)
4. Tools (list with purpose)
5. Output Format (structure of final deliverable)
6. Quality Gates (pre-output checklist)

---

## E2E Execution Flow

```
User invokes /quantum-circuit-design-assistant
│
├─ Step 1: sub-profile-intake
│   ├─ Ask 5 structured questions
│   ├─ Assign track (Beginner/Intermediate/Advanced)
│   └─ If insufficient info → apply conservative defaults
│
├─ Step 2: sub-concept-tutor (conditional)
│   ├─ If goal = "understand concepts" → teach all relevant modules in track
│   ├─ If goal = "design circuit" → teach prerequisite concepts only
│   ├─ If goal = "hardware selection" → skip to Step 4
│   └─ Quiz after each module; repeat if score < 70%
│
├─ Step 3: sub-circuit-designer (conditional)
│   ├─ If goal includes circuit design → run full circuit workflow
│   ├─ Validate gate sequence against platform connectivity
│   ├─ If circuit invalid → offer corrected version with explanation
│   └─ Always include both ASCII diagram and Qiskit code
│
├─ Step 4: sub-hardware-advisor (always)
│   ├─ WebSearch for latest platform specs if WebSearch available
│   ├─ If WebSearch unavailable → use SECOND-KNOWLEDGE-BRAIN.md + signal limitation
│   └─ Produce scored comparison table + recommendation
│
└─ Step 5: Main harness synthesis
    ├─ Compile full learning plan document
    ├─ Include all circuit outputs from Step 3
    ├─ Append hardware recommendation from Step 4
    ├─ List next 3 learning milestones with resources
    └─ Run quality gate checklist before output
```

**Error handling:**
- If user's circuit request is ambiguous → ask one clarifying question before proceeding
- If requested algorithm exceeds current NISQ hardware limits → warn explicitly and suggest error-mitigation or fault-tolerant alternatives
- If hardware data is stale (> 6 months) → flag and trigger WebSearch refresh

---

## SECOND-KNOWLEDGE-BRAIN Integration

The `SECOND-KNOWLEDGE-BRAIN.md` file serves as the internal knowledge cache for all sub-skills. It is consulted when WebSearch/WebFetch are unavailable and enriched by `tools/knowledge_updater.py` on a weekly schedule.

**Crawl Sources:**
- `https://arxiv.org/list/quant-ph/recent` — latest quantum physics papers
- `https://arxiv.org/list/quant-ph/month` — monthly digest
- `https://quantumai.google/blog` — Google Quantum AI announcements
- `https://learning.quantum.ibm.com/news` — IBM Quantum news
- `https://www.nature.com/npjqi/` — Nature Quantum Information
- `https://journals.aps.org/prl/` — Physical Review Letters (quantum hardware)
- `https://ionq.com/news` — IonQ hardware milestones
- `https://www.quantinuum.com/news` — Quantinuum announcements

**Append Format:**
```markdown
### [YYYY-MM-DD] {Title}
- **Authors:** {authors}
- **Venue:** {journal/conference/blog}
- **DOI/URL:** {doi or url}
- **Relevance:** {1-2 sentences: why this matters for the skill}
- **Key Finding:** {1-2 sentences: what was discovered/demonstrated}
```

---

## Supporting Tools Specification

### `tools/knowledge_updater.py`

**Purpose:** Automated weekly crawl to keep SECOND-KNOWLEDGE-BRAIN.md current with the latest quantum computing research and hardware advances.

**Inputs:**
- List of crawl sources (hardcoded + configurable)
- SECOND-KNOWLEDGE-BRAIN.md path (for deduplication and appending)
- Minimum relevance score threshold (default: 0.6)

**Outputs:**
- Updated SECOND-KNOWLEDGE-BRAIN.md with new entries appended
- Update log entry with date, number of new items, and sources crawled

**Deduplication:** SHA-256 hash of DOI or canonical URL; skip if hash already in knowledge base

**Schedule:** Weekly cron (recommended: Sundays 02:00 UTC)

---

## Quality Gates Definition

Before the main harness presents any final output, ALL of the following must be satisfied:

1. **Profile completeness:** Learner profile captured all 5 dimensions (background, goal, time budget, platform preference, specific interest)
2. **Citation coverage:** Every concept explanation cites at least one source from the evidence hierarchy (Nielsen & Chuang / Preskill > peer-reviewed journal > official platform docs > tutorials)
3. **Code validity:** All Qiskit code includes required imports, is syntactically complete, and includes measurement or state vector inspection
4. **Hardware accuracy:** All platform specs are sourced from publications or official docs within 12 months; stale data is flagged
5. **Track alignment:** Concept depth, circuit complexity, and hardware recommendations all match the user's assigned track
6. **Completeness of deliverable:** Final document includes (a) personalized learning plan, (b) circuit diagram(s) if circuit design was requested, (c) hardware recommendation, (d) next 3 milestones
7. **Graceful degradation signaled:** If WebSearch/WebFetch was unavailable, output explicitly notes which sections rely on cached knowledge

---

## Test Scenarios

(See `tests/test-scenarios.md` for full scenario details — 5+ scenarios included.)

### Summary

| # | Scenario | Track | Key Assertion |
|---|----------|-------|---------------|
| 1 | Python dev, no QM background, wants "start quantum" | Beginner | Bloch sphere explanation + Bell state circuit in Qiskit |
| 2 | Physics undergrad, needs Grover's algorithm circuit | Intermediate | Correct oracle + diffusion operator, ASCII + Qiskit, depth analysis |
| 3 | ML researcher, 50-qubit optimization, hardware selection | Advanced | Platform comparison table, IonQ vs IBM vs Quantinuum recommendation |
| 4 | Circuit with depth 200, needs NISQ-compatible version | Intermediate | Circuit compression recommendations, transpilation flags |
| 5 | User wants quantum error correction for logical qubit | Advanced | Steane code explanation, stabilizer formalism, surface code ASCII diagram |

---

## Key Design Decisions

1. **Nielsen & Chuang as the authoritative baseline:** Every concept explanation anchors to the canonical textbook before citing other sources, ensuring pedagogical rigor.
2. **Qiskit as the primary implementation language:** IBM Quantum's cloud platform offers the most accessible free tier; Qiskit is the most widely used framework; all circuit outputs default to Qiskit with notes on Cirq/PennyLane equivalents.
3. **ASCII circuit diagrams mandatory:** Graphical circuit tools require IDE plugins; ASCII diagrams work in any text output and are universally readable.
4. **Track-adaptive depth:** Three distinct learning tracks prevent both overwhelming beginners (with formalism they cannot absorb) and boring advanced users (with material they already know).
5. **Hardware-first reality check:** Every circuit design includes a hardware feasibility assessment — no circuit is presented without noting its NISQ vs. fault-tolerant status.
6. **Self-improving via ArXiv quant-ph:** The quantum computing field advances faster than any static textbook can track; weekly ArXiv crawls keep the skill's knowledge current.
7. **Graceful degradation documented:** Cloud-based tools (Qiskit Runtime, IBM Quantum cloud) frequently update their APIs; the skill explicitly flags when its Qiskit code may need version-specific adjustment.
8. **No unsubstantiated quantum speedup claims:** The skill explicitly teaches the distinction between theoretical quantum advantage and demonstrated practical quantum advantage, countering common misconceptions.
9. **Minimum 3 sub-skills enforced:** The sub-skill separation (intake / tutor / designer / advisor) ensures each workflow component is independently testable and reusable across the ai-ml cluster.
10. **Weekly crawl cadence:** Quantum hardware milestones are announced monthly (IBM's roadmap, Google's papers, IonQ's benchmarks); weekly crawl ensures no major announcement is missed.
