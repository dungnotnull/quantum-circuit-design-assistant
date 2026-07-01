---
name: quantum-circuit-design-assistant/sub-concept-tutor
description: Teach quantum computing concepts progressively using Nielsen & Chuang curricula, Bloch sphere visualizations, worked examples, Qiskit code, and comprehension quizzes
---

## Purpose

Deliver rigorous, citation-grounded, track-appropriate quantum computing concept instruction. This sub-skill ensures the learner builds genuine intuition and mathematical understanding — not superficial familiarity — before attempting circuit design or hardware selection. It adapts depth and formalism to the learner's track (Beginner / Intermediate / Advanced), includes textual Bloch sphere visualizations for all single-qubit operations, and verifies comprehension before proceeding.

---

## Inputs

- Learner profile from sub-profile-intake (track level, background, goal, time budget)
- Target concept(s) to teach in this session (from main harness based on goal)
- Any quiz history from earlier in the same session (to avoid re-testing known material)

---

## Module Map (7 Concept Modules)

| Module | Track | Topic | Nielsen & Chuang Reference |
|--------|-------|-------|--------------------------|
| 1 | Beginner | Qubits, superposition, Dirac notation, Born rule, measurement | Ch. 1.2-1.3, Ch. 2.1-2.2 |
| 2 | Beginner-Intermediate | Single-qubit gates (X, Y, Z, H, S, T, Rx, Ry, Rz); matrix representations; gate composition | Ch. 4.1-4.2 |
| 3 | Intermediate | Multi-qubit systems; tensor products; CNOT, Toffoli; entanglement; Bell states; GHZ states | Ch. 1.3, Ch. 4.3 |
| 4 | Intermediate | No-cloning theorem; quantum teleportation; dense coding | Ch. 1.3.7, Ch. 2.3 |
| 5 | Intermediate-Advanced | Quantum algorithms: Deutsch-Jozsa, Bernstein-Vazirani, Grover's search | Ch. 6 |
| 6 | Advanced | Shor's factoring; Quantum Fourier Transform (QFT); phase estimation | Ch. 5 |
| 7 | Advanced | Quantum error correction: stabilizer formalism, Steane code, surface codes, logical qubits | Ch. 10 |

---

## Workflow

For each concept module selected by the main harness, execute all four teaching components in order, then administer the comprehension quiz.

---

### Component A: Intuitive Analogy

Before any mathematics, build physical intuition with an analogy to something the learner already understands. The analogy must be honest — it illuminates the concept without misrepresenting the underlying physics.

**Module 1 analogy:** "Think of a classical bit as a coin that is either heads (0) or tails (1). A qubit is like a coin that is spinning in the air — it has a definite probability of landing heads or tails, but until it lands (measurement), it genuinely has both outcomes coexisting. Crucially, this is not just ignorance about which outcome will occur — quantum mechanics tells us the superposition is physically real."

**Module 2 analogy (gates):** "A classical NOT gate simply flips a bit from 0 to 1 or vice versa. Quantum gates are like rotations of the spinning coin in three dimensions. The Hadamard gate takes a coin pointing straight up (|0⟩) and rotates it to point horizontally (an equal superposition). The key difference: these are unitary operations — perfectly reversible, never losing information."

**Module 3 analogy (entanglement):** "When two qubits become entangled, measuring one instantly determines what you'll find when measuring the other — no matter how far apart they are. It's as if two coins were tossed together and 'agreed' to always land on opposite sides, but neither decided until observed. Einstein called this 'spooky action at a distance'; quantum mechanics says it's simply how correlated quantum states work."

**Module 5 analogy (Grover's):** "Grover's algorithm is like finding a name in an unsorted phone book. Classically, you must check entries one by one — on average N/2 tries. Grover uses amplitude amplification to make the target entry 'louder' with each iteration, finding it in √N steps. It's not magic — it's a carefully orchestrated interference pattern."

---

### Component B: Mathematical Formulation

Present the precise mathematical statement of the concept, calibrated to the learner's track.

**Beginner:** Use matrix notation sparingly; focus on state vector notation and probability; avoid density matrices and tensor products until Module 3.

**Intermediate:** Introduce matrix representations immediately; use Dirac notation fluently; cover tensor products from Module 3 onward.

**Advanced:** Use full Hilbert space formalism; introduce spectral decomposition, commutator relations, and Lie algebra structure of gate groups where relevant.

---

#### Module 1 (Beginner): Qubit and Measurement

State vector: |ψ⟩ = α|0⟩ + β|1⟩ where α, β ∈ ℂ, |α|² + |β|² = 1

Special states:
- |0⟩ = [1, 0]ᵀ (ground state; north pole on Bloch sphere)
- |1⟩ = [0, 1]ᵀ (excited state; south pole)
- |+⟩ = (|0⟩ + |1⟩)/√2 (positive x-axis)
- |−⟩ = (|0⟩ − |1⟩)/√2 (negative x-axis)

Born rule: P(outcome 0) = |α|², P(outcome 1) = |β|²
After measuring outcome 0: state collapses to |0⟩ (post-measurement state is not |ψ⟩)

---

#### Module 2: Single-Qubit Gates (Intermediate)

Each gate is a 2×2 unitary matrix U (U†U = I):

- X gate: [[0,1],[1,0]] — maps |0⟩→|1⟩, |1⟩→|0⟩ (quantum NOT)
- Y gate: [[0,-i],[i,0]] — maps |0⟩→i|1⟩, |1⟩→-i|0⟩
- Z gate: [[1,0],[0,-1]] — maps |+⟩→|−⟩ (phase flip, no effect on |0⟩ or |1⟩ individually up to global phase)
- H gate: [[1,1],[1,-1]]/√2 — maps |0⟩→|+⟩, |1⟩→|−⟩ (creates/destroys superposition)
- S gate: [[1,0],[0,i]] — π/2 phase rotation; S² = Z
- T gate: [[1,0],[0,e^(iπ/4)]] — π/4 phase; expensive in fault-tolerant computing; T† is Tdg
- Rotation gates: Rx(θ) = e^(-iθX/2), Ry(θ) = e^(-iθY/2), Rz(θ) = e^(-iθZ/2)

Gate composition: applying gate A then B is the matrix product BA|ψ⟩ (rightmost applied first in Dirac notation; leftmost applied first in circuit diagrams reading left to right).

---

#### Module 3: Entanglement and Bell States

Two-qubit state space: ℂ² ⊗ ℂ² = ℂ⁴
Basis: {|00⟩, |01⟩, |10⟩, |11⟩}

CNOT gate matrix (4×4):
```
[[1,0,0,0],
 [0,1,0,0],
 [0,0,0,1],
 [0,0,1,0]]
```
Effect: flips q1 (target) if q0 (control) = |1⟩

Bell state preparation: apply H to q0, then CNOT(q0→q1)
- Input: |00⟩
- After H on q0: (|0⟩+|1⟩)/√2 ⊗ |0⟩ = (|00⟩+|10⟩)/√2
- After CNOT: (|00⟩+|11⟩)/√2 = |Φ⁺⟩

Entanglement test: |Φ⁺⟩ cannot be written as |ψ_A⟩ ⊗ |ψ_B⟩ for any single-qubit states ψ_A, ψ_B — this is the definition of an entangled state.

---

### Component C: Bloch Sphere Visualization (Single-Qubit Concepts Only)

For all single-qubit gate concepts, provide a textual Bloch sphere visualization describing the initial state, the rotation axis and angle, and the final state.

**Template:**
```
Bloch Sphere — [Gate Name] acting on [initial state]

     |0⟩ (North Pole)
      │
      │ ← starting here
      │
──────┼──────   ← equator (|+⟩ left, |−⟩ right, |i⟩ front, |−i⟩ back)
      │
      │
     |1⟩ (South Pole)

Action: [Gate] rotates the state [θ] degrees around the [X/Y/Z/other] axis.
Result: [initial state] → [final state]
Coordinates: θ = [angle], φ = [angle]
```

**Worked examples:**

H gate on |0⟩:
- Rotates by 180° around the axis halfway between X and Z (i.e., the X+Z axis in the XZ plane)
- |0⟩ (north pole, θ=0) → |+⟩ (positive x-axis, θ=π/2, φ=0)
- This creates maximum superposition: equal probability of 0 or 1 upon measurement

X gate on |0⟩:
- Rotates by 180° around the X-axis
- |0⟩ (north pole) → |1⟩ (south pole)
- This is the quantum NOT gate

Rz(π/2) gate on |+⟩:
- Rotates by 90° around the Z-axis
- |+⟩ (positive x-axis, φ=0) → |i⟩ (positive y-axis, φ=π/2)
- This is the S gate

---

### Component D: Qiskit Demonstration Code

Provide complete, runnable Qiskit code demonstrating the concept. All code must:
- Include all required imports
- Use Qiskit 1.x API (QuantumCircuit, not deprecated legacy API)
- Include a simulation step (StatevectorSimulator or AerSimulator)
- Include comments explaining each line
- Produce observable output the learner can verify

---

#### Module 1 Demo: Qubit Superposition and Measurement

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Create a 1-qubit, 1-classical-bit circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard to create superposition: |0> -> |+> = (|0>+|1>)/sqrt(2)
qc.h(0)

# Measure the qubit into the classical bit
qc.measure(0, 0)

# Simulate 1000 shots to observe the probability distribution
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("Measurement results (1000 shots):")
print(counts)
# Expected output: approximately {'0': 500, '1': 500}
# This demonstrates that the H gate creates equal superposition:
# each shot independently collapses to 0 or 1 with 50% probability
```

---

#### Module 3 Demo: Bell State (Entanglement)

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit, 2-classical-bit circuit
qc = QuantumCircuit(2, 2)

# Step 1: Apply Hadamard to qubit 0 -> (|0>+|1>)/sqrt(2) tensored with |0>
qc.h(0)

# Step 2: Apply CNOT with qubit 0 as control, qubit 1 as target
# This entangles the qubits: result is Bell state |Phi+> = (|00>+|11>)/sqrt(2)
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Simulate
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("Bell state measurement results (1000 shots):")
print(counts)
# Expected: approximately {'00': 500, '11': 500}
# Notice: '01' and '10' never appear - the qubits are perfectly correlated!
# This demonstrates entanglement: measuring qubit 0 instantly determines qubit 1's value.
```

---

#### Module 5 Demo: Grover's Algorithm (2 qubits, target |11>)

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 2-qubit Grover's search for target state |11>
# Oracle marks |11> with a phase flip; diffusion operator amplifies it

qc = QuantumCircuit(2, 2)

# Initialization: create uniform superposition
qc.h([0, 1])

# --- Grover Iteration (1 iteration is optimal for N=4) ---

# Oracle for target |11>: applies a CZ gate (phase flip on |11>)
# CZ flips the phase of |11> only: |11> -> -|11>
qc.cz(0, 1)

# Diffusion operator (inversion about the average):
# H on all qubits, X on all qubits, multi-controlled Z, X on all, H on all
qc.h([0, 1])
qc.x([0, 1])
qc.cz(0, 1)
qc.x([0, 1])
qc.h([0, 1])

# --- End Grover Iteration ---

# Measure
qc.measure([0, 1], [0, 1])

simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("Grover's search results (target: |11>), 1000 shots:")
print(counts)
# Expected: '11' should appear in ~100% of shots (1 iteration is exact for N=4)
```

---

### Comprehension Quiz

After each module, administer 3 targeted questions. Adapt difficulty to the track.

**Module 1 Quiz (Beginner):**
1. "A qubit is in the state |ψ⟩ = (√3/2)|0⟩ + (1/2)|1⟩. What is the probability of measuring outcome 0?"
   - Answer: (√3/2)² = 3/4 = 75%
2. "After measuring a qubit in state |+⟩ and getting outcome 1, what is the post-measurement state?"
   - Answer: |1⟩ (state collapses to the measured eigenstate)
3. "True or false: A qubit in superposition contains both 0 and 1 simultaneously, and measurement reveals which value it 'already was.'"
   - Answer: False — according to the Copenhagen interpretation, the value is not determined until measurement; superposition is not merely ignorance about a pre-existing value.

**Module 3 Quiz (Intermediate):**
1. "What gate sequence prepares the Bell state |Ψ⁺⟩ = (|01⟩+|10⟩)/√2 starting from |00⟩?"
   - Answer: X on q1, then H on q0, then CNOT(q0→q1)
2. "If you measure qubit 0 of a Bell state |Φ⁺⟩ and get outcome 1, what state is qubit 1 in?"
   - Answer: |1⟩ (perfect correlation)
3. "The CNOT gate on 2 qubits is represented by what 4×4 matrix? What does it do to the basis state |10⟩?"
   - Answer: Maps |10⟩ to |11⟩ (flips the target qubit when control is |1⟩)

**Module 5 Quiz (Intermediate-Advanced):**
1. "Grover's algorithm provides a quadratic speedup. For a database of 1,000,000 entries, how many oracle queries does Grover's require (approximately)?"
   - Answer: O(√1,000,000) = O(1000) queries
2. "What are the two main components of a Grover iteration, and what does each do?"
   - Answer: (1) Oracle — marks the target state with a phase flip; (2) Diffusion operator — reflects all amplitudes around their average, amplifying the target amplitude
3. "Why can't you run Grover's algorithm for too many iterations beyond the optimal √N?"
   - Answer: The amplitude of the target state oscillates sinusoidally — running past the peak (at ~π√N/4 iterations) causes it to de-amplify back toward uniform superposition.

---

**Quiz Evaluation:**
- Score 3/3: Proceed to next module or circuit design
- Score 2/3: Briefly re-explain the missed concept; proceed
- Score 1/3 or 0/3: Re-teach the module using an alternative analogy before proceeding
- Never skip the quiz — comprehension verification is mandatory per the quality gate

---

## Outputs

For each concept module taught, produce:

1. **Concept Brief:** Structured explanation covering all four components (analogy, math, Bloch sphere, code)
2. **Cited Source:** The specific Nielsen & Chuang chapter, ArXiv paper, or official curriculum module referenced
3. **Quiz Q&A:** The 3 questions asked, the learner's responses, and correctness assessment
4. **Comprehension Score:** X/3 correct
5. **Next Concept Recommendation:** Which module to cover next, or "Proceed to circuit design" if prerequisites are met
6. **Prerequisite Flag (if any):** If during teaching a new prerequisite gap is identified, flag it immediately

---

## Quality Gate

This sub-skill's output is accepted when:

1. Every concept explanation cites at least one source from the evidence hierarchy (Nielsen & Chuang / Preskill > peer-reviewed journal > official platform docs > tutorials). No factual assertions without citations.
2. Bloch sphere visualization is provided for every single-qubit gate concept.
3. All Qiskit code is syntactically valid, uses Qiskit 1.x API, includes imports, and includes measurement or statevector inspection.
4. Comprehension quiz is administered after each module — never skipped.
5. If quiz score is < 2/3, an alternative explanation is attempted before proceeding.
6. Mathematical depth is appropriate to the learner's track (no graduate formalism for Beginner track without explicit scaffolding).
