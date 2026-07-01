---
name: quantum-circuit-design-assistant/sub-profile-intake
description: Structured learner intake for quantum computing education — assesses background, goal, platform preference, and time budget to assign a learning track
---

## Purpose

Establish a complete learner profile before any quantum computing teaching or circuit design begins. The profile determines which concept modules to teach, the appropriate depth of mathematical formalism, which hardware platforms to discuss, and how to prioritize session time.

Without an accurate profile, the harness risks either overwhelming beginners with graduate-level formalism or boring advanced learners with material they already know. This sub-skill runs exactly once per session, at the very beginning.

---

## Inputs

- User's opening message (free text — may already contain clues about background and goals)
- Any prior session context (if user mentions previous sessions or existing knowledge)

---

## Workflow

### Step 1: Infer from Opening Message

Before asking questions, attempt to infer answers from the user's opening message:

- **Background clues:** Mentions of degree (physics, CS, math, engineering), job role (software developer, researcher, student), or self-described level ("I'm a complete beginner," "I know linear algebra")
- **Goal clues:** Phrases like "I want to understand," "I need to design," "which hardware should I use," "I'm implementing Grover's algorithm"
- **Platform clues:** Mentions of Qiskit, Cirq, IBM, Google, IonQ, Q#
- **Topic clues:** Specific algorithm names, gate types, or hardware names mentioned

For each dimension where the opening message provides clear evidence, skip that question. Ask only the remaining questions.

---

### Step 2: Structured Intake Questions

Ask only the unanswered questions from this set. If the user's opening message answered all 5, skip directly to Step 3.

**Q1 — Background Level (if not inferred):**
> "To tailor this session to you: what's your background with physics, mathematics, and computer science? For example:
> - No QM/linear algebra (complete beginner)
> - Some linear algebra, basic programming (self-taught or early undergrad)
> - Physics or math undergrad (comfortable with complex numbers, matrices, Dirac notation)
> - Graduate level or professional (quantum mechanics, tensor products, Hilbert spaces)"

**Q2 — Primary Learning Goal (if not inferred):**
> "What's your main goal for this session?
> - Understand quantum computing concepts (theory, intuition, key ideas)
> - Design a specific quantum circuit (please describe which algorithm or problem)
> - Select the right quantum hardware for my project
> - All of the above — full quantum computing introduction
> - Something else (please describe)"

**Q3 — Specific Topic or Algorithm (if not inferred):**
> "Do you have a specific topic, algorithm, or problem in mind? (e.g., Bell states, Grover's search, Shor's factoring, quantum chemistry, QAOA, quantum error correction, or 'no preference — teach me from the start')"

**Q4 — Hardware Preference (if not inferred):**
> "Do you have a preferred quantum computing platform or toolchain?
> - IBM Quantum / Qiskit (most accessible free tier)
> - Google / Cirq
> - IonQ (trapped ion)
> - Microsoft / Q# (Azure Quantum)
> - No preference — recommend the best for my use case"

**Q5 — Time Budget (if not inferred):**
> "Roughly how much time do you have for this session and for ongoing learning?
> - This session only (30-60 minutes)
> - A few hours per week for several weeks
> - I'm building toward research/professional work (months of dedicated study)
> - Just exploring — no time commitment yet"

---

### Step 3: Track Assignment

Based on the intake responses, assign the learner to one of three tracks:

**Beginner Track:**
- Criteria: No prior QM or linear algebra; "complete beginner" self-identification; CS background only without formal math
- What this means: Start with qubits and superposition using physical intuition and analogies before introducing matrix notation; use only the Bloch sphere description without the full density matrix formalism; circuits use only H, X, CNOT
- Nielsen & Chuang starting point: Chapter 1 (Introduction)

**Intermediate Track:**
- Criteria: Knows linear algebra, complex numbers, and basic probability; physics or math undergrad; has programmed before
- What this means: Introduce matrix representations of gates immediately; use Dirac notation fluently; cover multi-qubit systems and entanglement; target Grover's algorithm as the capstone
- Nielsen & Chuang starting point: Chapter 2 (Linear Algebra) or Chapter 4 (Quantum circuits)

**Advanced Track:**
- Criteria: Graduate physics or QC background; has worked with unitary matrices, Hilbert spaces, tensor products; may have prior Qiskit experience
- What this means: Skip introductory material; engage immediately with circuit optimization, error correction, hardware constraints, algorithm implementation details, and NISQ vs FTQC trade-offs
- Nielsen & Chuang starting point: Chapter 5+ (Quantum algorithms) or Chapter 10 (Error correction)

**Conservative defaults if user declines all questions:**
- Track: Beginner
- Platform: Qiskit (IBM Quantum)
- Goal: Full introduction
- Time: Session-only

---

### Step 4: Prerequisite Gap Identification

Based on the track assignment and stated goal, identify any prerequisite gaps that must be addressed before the learner's stated goal is achievable:

| Stated Goal | Track | Common Gaps | Resolution |
|-------------|-------|-------------|-----------|
| "Implement Shor's algorithm" | Beginner | Missing: superposition, gates, QFT, phase estimation, modular arithmetic | Must complete Modules 1-6 first; set realistic multi-session expectation |
| "Design Bell state circuit" | Beginner | None (achievable in one session) | Proceed directly |
| "Optimize my 50-qubit VQE circuit" | Intermediate | Missing: hardware connectivity specifics, noise mitigation | Skip basic gates; focus on hardware-aware circuit design |
| "Understand surface codes" | Intermediate | Missing: stabilizer formalism prerequisite | Teach stabilizers before surface codes |

Communicate gaps constructively: "To reach your goal of [X], we'll first cover [prerequisite], which typically takes [Y]. This session will [achieve Z] and set you up for [X] in a subsequent session."

---

### Step 5: Session Scope Setting

Based on profile and time budget, set realistic scope for this session:

- **Session only (30-60 min):** Cover 1-2 concept modules maximum; design 1 simple circuit; brief hardware recommendation
- **Several hours/week:** Full module sequence for the track; 2-3 circuit examples with optimization; complete hardware comparison
- **Research/professional:** Focus on the specific gap in the user's knowledge; no time wasted on known material; hardware deep-dive appropriate to their research domain
- **Just exploring:** Light introduction to 2-3 key concepts with 1 circuit example; emphasize the "what is quantum computing" framing before any formalism

---

## Outputs

### Learner Profile (JSON-like summary)

```
LEARNER PROFILE
===============
Background:     [No QM | Some linear algebra | Physics/Math undergrad | Graduate/Professional]
Goal:           [Concepts | Circuit design (algorithm: X) | Hardware selection | Full intro | Other]
Specific Topic: [Bell states | Grover's | Shor's | QEC | QAOA | None specified]
Platform:       [IBM/Qiskit | Google/Cirq | IonQ | Microsoft/Q# | Platform-agnostic]
Time Budget:    [Session-only | Few hours/week | Research commitment | Exploring]

TRACK ASSIGNED: [Beginner | Intermediate | Advanced]

PREREQUISITE GAPS:
- [Gap 1 if any]
- [Gap 2 if any]
- (None identified)

SESSION SCOPE:
- [What will be covered this session]
- [What is deferred to future sessions]
```

---

## Quality Gate

This sub-skill's output is accepted when:

1. All 5 profile dimensions are captured (background, goal, specific topic, platform, time budget) — either from the user's answers or from justified conservative defaults
2. Track assignment is explicitly stated (Beginner / Intermediate / Advanced) with a one-line justification
3. Prerequisite gap analysis is completed for the user's stated goal
4. Session scope is set and communicated to the user before proceeding to Step 2 of the main harness
5. No assumptions are made about the user's knowledge that are not either confirmed or defaulted conservatively
