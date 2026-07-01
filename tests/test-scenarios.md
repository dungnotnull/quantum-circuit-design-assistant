# test-scenarios.md — Quantum Circuit Design Learning Assistant (Skill #245)

## Overview

This file contains 6 test scenarios covering distinct user archetypes, learning goals, and skill workflow paths. Each scenario specifies: input (what the user says), expected behavior (which sub-skills are invoked and in what order), expected outputs (what the final deliverable must contain), pass criteria, common failure modes, and which quality gates are exercised.

Scenarios are ordered from simplest (Beginner / single goal) to most complex (Advanced / multi-goal).

---

## Scenario 1: Python Developer — First Contact with Quantum Computing

### User Profile
- **Background:** Software engineer, 5 years Python experience, no physics or math beyond high school
- **Goal:** Understand what quantum computing is and see a real circuit
- **Platform:** No preference
- **Time:** Just exploring today

### User Input
> "I'm a Python developer and everyone is talking about quantum computing. I have zero physics knowledge. Can you help me understand what it is and show me the simplest possible quantum circuit?"

### Expected Sub-skill Invocation Sequence
1. **sub-profile-intake** — infers Python background from message; confirms no QM background; assigns Beginner track; goal = full intro; platform = IBM/Qiskit (conservative default)
2. **sub-concept-tutor** — Module 1 (qubit, superposition, Bloch sphere, Born rule) + Module 2 (H gate, X gate) — Beginner depth
3. **sub-circuit-designer** — Bell state circuit (simplest entangled circuit showing 2-qubit gates)
4. **sub-hardware-advisor** — recommends IBM Quantum free tier with Qiskit; brief comparison

### Expected Outputs

**Learner Profile:**
```
Track: Beginner
Background: Python developer, no QM/physics
Goal: Full introduction
Platform: IBM Quantum / Qiskit (default)
Time: Session-only
```

**Concept Summary:**
- Qubit vs. classical bit analogy (spinning coin)
- Superposition with |ψ⟩ = α|0⟩ + β|1⟩ notation (introduced gently, not derived)
- Bloch sphere description: "|0⟩ is the north pole; |+⟩ is pointing in the positive x-direction"
- Born rule explained: "probability of measuring 0 is |α|²"
- H gate described as "rotating the north pole to the equator"
- CNOT gate described as "quantum controlled NOT — if the first qubit is |1⟩, flip the second"
- At least 1 citation: Nielsen & Chuang Chapter 1

**Circuit (Bell State):**
```
q0: ─[H]─────■─────[M]─
             │
q1: ─────────X─────[M]─
```

**Qiskit Code (complete, runnable):**
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

simulator = AerSimulator()
job = simulator.run(transpile(qc, simulator), shots=1000)
result = job.result()
print(result.get_counts())
# Expected: {'00': ~500, '11': ~500}
print(qc.draw('text'))
```

**Hardware Recommendation:** IBM Quantum free tier; step-by-step IBM Quantum account creation

**Next Milestones:**
1. Complete Module 3 (Entanglement, multi-qubit systems)
2. Try running the Bell circuit on IBM Quantum free tier
3. Study Module 5 (Grover's algorithm) — the first practically interesting algorithm

### Pass Criteria
- [ ] Track correctly assigned as Beginner
- [ ] No density matrices, no tensor product notation in concept explanations (inappropriate for Beginner)
- [ ] Bloch sphere described textually (not using formal spherical coordinates for Beginner)
- [ ] Bell state ASCII diagram is correct (H on q0, CNOT control=q0 target=q1)
- [ ] Qiskit code includes imports, circuit, measurement, and simulation
- [ ] At least 1 citation to Nielsen & Chuang Chapter 1
- [ ] Hardware recommendation includes free-tier access instructions
- [ ] Quiz administered after Module 1 (at minimum)
- [ ] 3 next milestones provided with resource references

### Common Failure Modes
- **Over-formalization:** Using bra-ket notation extensively without explanation for a Python-background user
- **Missing Bloch sphere:** Skipping the textual Bloch sphere description
- **Incomplete Qiskit code:** Providing circuit construction but no simulation
- **D-Wave confusion:** Mentioning D-Wave as "quantum computing" without clarifying it's a different paradigm

### Quality Gates Exercised
- Profile completeness (Gate 1)
- Citation coverage (Gate 2)
- Code validity (Gate 3)
- Track alignment (Gate 5)
- Deliverable completeness (Gate 6)

---

## Scenario 2: Physics Undergraduate — Grover's Algorithm Circuit Design

### User Profile
- **Background:** 3rd year physics undergraduate, comfortable with linear algebra, Dirac notation, and basic QM
- **Goal:** Design a complete 3-qubit Grover's algorithm circuit for target state |101⟩
- **Platform:** IBM Quantum (already has account, uses Qiskit)
- **Time:** Several hours per week, building toward research

### User Input
> "I'm a physics undergrad. I know linear algebra, Dirac notation, and some quantum mechanics from my coursework. I want to design a Grover's algorithm circuit for 3 qubits, searching for the state |101⟩. I use Qiskit. Can you build the complete circuit with the oracle and diffusion operator, and tell me if it'll run on IBM hardware?"

### Expected Sub-skill Invocation Sequence
1. **sub-profile-intake** — infers Intermediate track (physics background + linear algebra); goal = circuit design; platform = IBM/Qiskit; no gap identified for Grover's (has prerequisite knowledge)
2. **sub-concept-tutor** — Brief Module 5 review: oracle concept, amplitude amplification, optimal iteration count (1 question quiz only; skip basics they know)
3. **sub-circuit-designer** — Full Grover's circuit: initialization, oracle for |101⟩, diffusion operator, n_iterations = floor(π/4 × √8) = 2; ASCII diagram, Qiskit code, circuit metrics, IBM connectivity check
4. **sub-hardware-advisor** — IBM Quantum hardware recommendation (verify 3-qubit support, heavy-hex check, fidelity)

### Expected Outputs

**Concept Review (brief):**
- Oracle for |101⟩: phase flip on target state using X gates + Toffoli
- Diffusion operator: H, X, multi-controlled Z, X, H sequence
- Optimal iterations: n = ⌊π/4 × √8⌋ = 2

**Gate Sequence Table:**

| Step | Gate | Qubits | Purpose |
|------|------|--------|---------|
| 1-3 | H | q0, q1, q2 | Uniform superposition |
| 4 | X | q1 | Pre-condition oracle (|101⟩ has q1=0, flip to 1 for oracle) |
| 5-7 | Oracle (Toffoli-based) | q0, q1, q2 | Phase flip on |101⟩ |
| 8 | X | q1 | Undo oracle pre-condition |
| 9-11 | H | q0, q1, q2 | Diffusion step 1 |
| 12-14 | X | q0, q1, q2 | Diffusion step 2 |
| 15 | H | q2 | Diffusion: multi-controlled Z via HCCXHon q2 |
| 16 | CCX | q0,q1,q2 | Diffusion: multi-controlled Z |
| 17 | H | q2 | Diffusion: restore |
| 18-20 | X | q0, q1, q2 | Diffusion step 4 |
| 21-23 | H | q0, q1, q2 | Diffusion step 5 |
| Repeat steps 4-23 for second iteration | | | |
| 24-26 | Measure | q0,q1,q2 | Readout |

**ASCII Circuit:**
```
q0: ─[H]─────────■──[H]─[X]─────■──[X]─[H]─[M]─  (× 2 iterations)
                 │               │
q1: ─[H]─[X]─────●──[X]─[H]─[X]─────■──[X]─[H]─[M]─
                 │               │
q2: ─[H]──────[CCX]──[H]─[X]─[H]─[CCX]─[H]─[X]─[H]─[M]─
     Init  Oracle        Diffusion
```

**Qiskit Code:** Complete implementation matching sub-circuit-designer Module 5 reference

**Circuit Metrics:**
```
Qubits: 3
Circuit depth: ~18 (per iteration) × 2 iterations = ~36
Single-qubit gates: ~20
Two-qubit gates (CX/CCX): ~6 (CCX = 3 CNOTs each = 12 effective CNOTs per iteration)
T-gate count: 0 (no T gates in this decomposition)
NISQ Classification: NISQ-feasible (depth 36, 3 qubits — well within IBM Heron limits)
```

**IBM Connectivity Check:**
- 3-qubit linear connectivity sufficient for this circuit (q0-q1-q2 path available on Eagle/Heron)
- CCX decomposes to 6 CNOTs in standard Qiskit decomposition; heavy-hex supports q0→q1 and q1→q2 natively

### Pass Criteria
- [ ] Track correctly assigned as Intermediate (no Beginner-level scaffolding for basic gates)
- [ ] Oracle correctly targets |101⟩ (X on q1, then CCX, then X on q1)
- [ ] Optimal iteration count is 2 (not 1 or 3)
- [ ] Qiskit code is complete, runnable, and produces ~|101⟩ as the dominant measurement outcome
- [ ] Circuit depth and 2-qubit gate counts are computed
- [ ] IBM connectivity check explicitly confirms circuit is feasible on Eagle/Heron without extra SWAPs
- [ ] Citation to Grover (1996) or Nielsen & Chuang Chapter 6 included
- [ ] At least 2 optimization suggestions provided (e.g., gate cancellations across iterations, optimization_level=3 transpilation)

### Common Failure Modes
- **Wrong oracle construction:** Failing to flip q1 (which is 0 in |101⟩) before and after the Toffoli
- **Wrong iteration count:** Using n=1 (optimal for N=4) instead of n=2 (optimal for N=8)
- **Incomplete circuit:** Oracle without diffusion operator, or vice versa
- **Missing metrics:** Providing code but not computing depth, gate counts, and NISQ classification

### Quality Gates Exercised
- Citation coverage (Gate 2)
- Code validity (Gate 3)
- Hardware accuracy (Gate 4)
- Track alignment (Gate 5)
- Deliverable completeness (Gate 6)

---

## Scenario 3: ML Researcher — 50-Qubit Hardware Selection

### User Profile
- **Background:** ML researcher with strong Python skills; has read about quantum ML; no hands-on quantum experience
- **Goal:** Select the best quantum hardware for running a 50-qubit variational circuit (VQE/QAOA hybrid)
- **Platform:** No preference — wants the best fit for research
- **Time:** Research commitment (months of dedicated study)

### User Input
> "I'm an ML researcher exploring quantum machine learning. I need to run variational quantum circuits for a quantum optimization problem — roughly 50 qubits, parameterized Ry and CNOT layers, moderate circuit depth (around 20-30 layers). I want to compare quantum hardware options and understand the trade-offs. I'm not committed to any platform yet. Budget: can use academic access or AWS Braket, but not the most expensive options."

### Expected Sub-skill Invocation Sequence
1. **sub-profile-intake** — ML researcher background → Intermediate track (no QM experience, but strong general CS/math skills); goal = hardware selection; 50-qubit VQE; budget-conscious
2. **sub-concept-tutor** — Brief Module on variational algorithms (VQE/QAOA): parameterized circuits, ansatz, cost function, NISQ suitability (skip basic gate theory; they need context for their use case)
3. **sub-circuit-designer** — Brief circuit sketch of 2-layer QAOA ansatz (not full 50-qubit — illustrate the pattern): metrics analysis showing that 50-qubit depth-30 circuits are NISQ-challenging
4. **sub-hardware-advisor** — Full comparison of IBM Eagle/Heron, IonQ Forte, Rigetti Ankaa-2 for 50-qubit VQE; exclude Google (no public access) and Quantinuum (too expensive for 50Q regular use)

### Expected Outputs

**Hardware Comparison Table (50-qubit VQE focus):**

| Platform | 50Q Support | Connectivity for VQE | Gate Fidelity | Access | Cost | Research Fit | Total |
|----------|-------------|---------------------|--------------|--------|------|-------------|-------|
| IBM Eagle R3 (127q) | Yes | 3/5 (heavy-hex limits; needs SWAPs for all-to-all layers) | 4/5 | 5/5 (free + academic) | 5/5 | 4/5 | 26/30 |
| IonQ Forte (36q) | Partial (36<50) | 5/5 (all-to-all) | 4/5 | 3/5 (Braket pricing) | 3/5 | 4/5 | 24/30 |
| Rigetti Ankaa-2 (84q) | Yes | 4/5 (octagonal > heavy-hex) | 3/5 | 3/5 (Braket) | 3/5 | 3/5 | 20/30 |

**Recommendation:** IBM Eagle R3 for 50-qubit VQE — free academic tier, Qiskit ecosystem for VQE/QAOA, sufficient qubits; use Qiskit Runtime Primitives (Estimator V2) for variational workflows.

**Key Insight on NISQ-Challenging Classification:**
- 50-qubit, depth-30 circuit with CNOT layers: expected depth after heavy-hex SWAP insertion ≈ 60-90
- T2 ≈ 200 µs, CNOT gate time ≈ 300 ns → 60-layer budget ≈ 18 µs well within T2 but fidelity decay is cumulative
- Noise mitigation recommendation: ZNE + M3 measurement mitigation for reliable results

### Pass Criteria
- [ ] At least 3 platforms compared
- [ ] IBM Eagle R3 identified as primary recommendation for academic/cost-constrained 50Q VQE
- [ ] Heavy-hex connectivity limitation for VQE explicitly noted with SWAP overhead estimate
- [ ] NISQ-challenging classification for 50-qubit depth-30 circuits
- [ ] ZNE and M3 error mitigation recommended for IBM
- [ ] IonQ noted as excellent for connectivity but insufficient qubit count (36 < 50)
- [ ] Google Quantum AI noted as unavailable for public use
- [ ] Quantinuum noted as highest fidelity but most expensive — suitable for smaller circuits

### Common Failure Modes
- **Recommending Google Sycamore:** Not publicly accessible
- **Ignoring qubit count limits:** IonQ Forte has only 36 qubits — cannot run 50-qubit circuits
- **Missing SWAP overhead analysis:** Heavy-hex requires significant SWAP insertion for VQE layers, dramatically increasing circuit depth
- **No noise mitigation guidance:** 50-qubit VQE on NISQ hardware requires ZNE or similar; bare results will be meaningless without mitigation

### Quality Gates Exercised
- Hardware accuracy (Gate 4) — must cite platform specs from official sources
- Deliverable completeness (Gate 6)
- Graceful degradation (Gate 7) — if WebSearch unavailable, must flag stale hardware data

---

## Scenario 4: Circuit Depth Optimization Challenge

### User Profile
- **Background:** Intermediate — quantum computing student, knows Qiskit
- **Goal:** Reduce a circuit from depth 200 to under depth 60 for IBM Eagle hardware
- **Platform:** IBM Eagle R3

### User Input
> "I have a quantum circuit that currently has depth 200 and about 80 CNOT gates for a 15-qubit simulation. I need to get it under depth 60 to fit within IBM Eagle's coherence window. The circuit implements a Hamiltonian simulation. What optimizations can I apply?"

### Expected Sub-skill Invocation Sequence
1. **sub-profile-intake** — Intermediate; specific optimization goal; IBM Eagle
2. **sub-concept-tutor** — Brief: NISQ circuit depth limits, T2 budget, why depth matters (1 specific concept, no quiz for this technical user)
3. **sub-circuit-designer** — Optimization analysis for a 15-qubit depth-200 circuit targeting IBM Eagle
4. **sub-hardware-advisor** — IBM Eagle specifications relevant to depth budget

### Expected Outputs

**Depth Budget Analysis:**
```
IBM Eagle R3 Coherence Budget:
  T2 (dephasing): ~200 µs
  CNOT gate time: ~300 ns
  Single-qubit gate time: ~50 ns

Maximum safe circuit depth (50% fidelity budget):
  Pure CNOT circuit: 200 µs / 300 ns ≈ 666 CNOTs (theoretical)
  Realistic budget (accounting for readout + overhead): ~100 CNOTs
  Your circuit: 80 CNOTs / depth 200 — depth is the bottleneck, not CNOT count

Conclusion: Depth reduction from 200 → 60 is achievable via parallelization and compilation.
```

**Optimization Recommendations (ordered by impact):**

1. **Qiskit transpilation level 3** (impact: high, effort: none)
   ```python
   from qiskit import transpile
   optimized = transpile(circuit, backend=ibm_eagle_backend, optimization_level=3)
   print(f"Depth after level-3 transpilation: {optimized.depth()}")
   ```
   Expected improvement: 20-40% depth reduction for typical circuits

2. **Gate parallelization analysis** (impact: high, effort: medium)
   - Identify gates acting on independent qubits that can execute simultaneously
   - Restructure Hamiltonian Pauli term ordering to maximize parallelism

3. **Cartan decomposition / KAK decomposition** (impact: high for 2Q blocks, effort: high)
   - Any 2-qubit unitary can be decomposed into at most 3 CNOTs
   - If Hamiltonian simulation uses more, check for redundancy

4. **TKET compiler** (impact: medium-high, effort: low)
   ```python
   from pytket import Circuit
   from pytket.extensions.qiskit import qiskit_to_tk, tk_to_qiskit
   from pytket.passes import FullPeepholeOptimise, auto_rebase_pass
   tk_circ = qiskit_to_tk(circuit)
   FullPeepholeOptimise().apply(tk_circ)
   print(f"Depth after TKET: {tk_circ.depth()}")
   ```

5. **Dynamical decoupling** (impact: medium, effort: low)
   - Does not reduce depth but mitigates T2 dephasing for idle qubits
   - Net effect: same depth circuit achieves higher fidelity

6. **Circuit cutting (if depth target still not met)** (impact: variable, effort: high)
   - Cut 15-qubit circuit into 2 subcircuits of 8 qubits
   - Use Qiskit CircuitKnitting toolbox
   - Trade-off: 2^k overhead in shots for k cuts

### Pass Criteria
- [ ] Concrete analysis of IBM Eagle's T2 and gate time budget
- [ ] At least 4 specific optimization techniques with code
- [ ] Optimization level 3 transpilation shown as the first recommendation (easy win)
- [ ] TKET as an alternative compiler explicitly mentioned with code
- [ ] Circuit cutting mentioned as last resort (significant overhead)
- [ ] Final projected depth after recommended optimizations stated (or range given)
- [ ] NISQ-challenging classification maintained (depth 60 is still challenging for 15-qubit simulation)

### Common Failure Modes
- **Only generic advice:** "Use optimization_level=3" without explaining WHY it helps
- **Missing TKET:** TKET is frequently better than Qiskit transpiler for deep circuits on specific topologies
- **No coherence analysis:** Not connecting the depth target to T2/gate-time budget
- **Overconfident about target:** Claiming depth 60 is guaranteed when it depends on circuit structure

### Quality Gates Exercised
- Code validity (Gate 3)
- Hardware accuracy (Gate 4) — IBM Eagle T2 and gate times must be cited or noted as approximate
- Track alignment (Gate 5) — Intermediate; technical detail appropriate

---

## Scenario 5: Advanced — Quantum Error Correction (Logical Qubit)

### User Profile
- **Background:** Graduate physics student, studied quantum information theory, familiar with stabilizer codes
- **Goal:** Understand and design the [[7,1,3]] Steane code; ASCII circuit for syndrome measurement; surface code comparison
- **Platform:** Academic understanding (no hardware target)
- **Time:** Research commitment

### User Input
> "I'm a PhD student in quantum information. I need a thorough explanation of the [[7,1,3]] Steane code — logical qubit encoding circuit, syndrome measurement procedure, and how to correct a single-qubit error. Also compare it to surface codes for fault-tolerant quantum computing. I know the stabilizer formalism."

### Expected Sub-skill Invocation Sequence
1. **sub-profile-intake** — Advanced track (PhD student, knows stabilizer formalism); goal = QEC concepts + circuit design; no hardware target needed
2. **sub-concept-tutor** — Module 7 (Advanced): Steane code generators, logical operators, encoding circuit; surface code comparison; no basic scaffolding needed
3. **sub-circuit-designer** — Steane code encoding circuit (7 physical qubits → 1 logical qubit); syndrome measurement circuit (ancilla qubits); error correction lookup table
4. **sub-hardware-advisor** — Brief: hardware requirements for fault-tolerant QC (logical qubit overhead); Quantinuum H2 as best current platform for small QEC demonstrations

### Expected Outputs

**Steane Code Explanation:**
- Generators: X-type (X₁X₂X₄, X₂X₃X₆, X₁X₃X₇, X₃X₄X₅X₆X₇) and Z-type (same pattern)
- Logical |0_L⟩ and |1_L⟩: linear combinations of all weight-4 and weight-8 codewords
- Distance d=3: can detect 2 errors, correct 1 error
- Encoding: 7 qubits, 6 ancillas for syndrome measurement, 1 physical qubit → 1 logical qubit

**Steane Code Syndrome Measurement Circuit (abbreviated ASCII):**
```
|0>_L encoding circuit (7 data qubits):

q0(data): ─[H]─────────■─────────────■──────────────
q1(data): ─[H]─────────│──■──────────│──■────────────
q2(data): ─────────────│──│──[H]─────│──│──■──────────
q3(data): ─────────────X──│──────────│──│──│─────────
q4(data): ─────────────│──X──────────│──│──│─────────
q5(data): ─────────────│──│──────────X──│──│─────────
q6(data): ─────────────│──│────────────X──│─────────

(Complete Steane encoding circuit has 6 CNOT gates from the 3 generator qubits)
```

**Comparison Table: Steane [[7,1,3]] vs Surface Code:**

| Property | Steane [[7,1,3]] | Surface Code |
|----------|-----------------|--------------|
| Physical qubits per logical | 7 | ~1000 at practical error rates |
| Distance | 3 (corrects 1 error) | d=3 requires 17 qubits; scales as d² |
| Error threshold | ~1% (depends on noise model) | ~1% (2D layout) |
| CNOT connectivity | Non-local (requires all-to-all or SWAP overhead) | Local (nearest-neighbor 2D grid) |
| Gate transversality | All Clifford gates transversal; T requires magic state distillation | Limited transversal gates |
| Current hardware suitability | 7 qubits; demonstrated on trapped ion (IBM, Quantinuum) | Leading for superconducting scale-up (IBM roadmap) |
| Best platform | Trapped ion (IonQ, Quantinuum) — all-to-all solves connectivity | Superconducting (IBM, Google) — 2D grid matches surface code topology |

**Qiskit Steane Encoding Circuit:**
```python
from qiskit import QuantumCircuit

def steane_encoding_circuit() -> QuantumCircuit:
    """
    Encode 1 logical qubit into 7 physical qubits using the Steane [[7,1,3]] code.
    Logical |0_L> = (1/sqrt(8)) * sum of all even-weight codewords.
    Input: q0 in arbitrary state |psi> = alpha|0> + beta|1>; q1-q6 in |0>
    """
    qc = QuantumCircuit(7, name="Steane Encoding")
    # Apply Hadamard to qubits 0, 1, 2 (generator qubits for X-stabilizers)
    qc.h([0, 1, 2])
    # CNOT gates from generator protocol (parity check matrix rows)
    # Row 1: qubits 0,3,4,6 share X parity
    qc.cx(0, 3)
    qc.cx(0, 4)
    qc.cx(0, 6)
    # Row 2: qubits 1,3,5,6 share X parity
    qc.cx(1, 3)
    qc.cx(1, 5)
    qc.cx(1, 6)
    # Row 3: qubits 2,4,5,6 share X parity
    qc.cx(2, 4)
    qc.cx(2, 5)
    qc.cx(2, 6)
    return qc

encoding_circuit = steane_encoding_circuit()
print(encoding_circuit.draw('text'))
print(f"Encoding circuit depth: {encoding_circuit.depth()}")
print(f"CNOT count: {encoding_circuit.count_ops().get('cx', 0)}")
```

### Pass Criteria
- [ ] Track correctly assigned as Advanced (no introductory scaffolding)
- [ ] Steane code generators correctly stated (X-type and Z-type, 6 generators total)
- [ ] Encoding circuit is physically correct (produces logical |0_L⟩ with correct Hadamard + CNOT structure)
- [ ] Syndrome measurement procedure explained (6 ancilla qubits, 6 syndrome bits, Pauli error correction)
- [ ] Error correction lookup table referenced (2^6 = 64 possible syndromes; 21 non-trivial single-qubit errors + identity)
- [ ] Surface code comparison addresses: overhead (1000× physical qubits), threshold (~1%), topology match
- [ ] Citation to Steane (1996) and Fowler et al. (2012) for surface codes
- [ ] Hardware recommendation identifies Quantinuum H2 (all-to-all, highest 2Q fidelity) as best for Steane code; IBM/Google for surface codes

### Common Failure Modes
- **Wrong generator count:** Steane code has 6 generators (3 X-type + 3 Z-type), not 4 or 7
- **Encoding circuit for wrong logical state:** Must produce |0_L⟩ (superposition of even-weight codewords), not an arbitrary state
- **Over-simplifying surface code comparison:** "Surface code is better" without explaining the trade-offs (transversality, overhead, connectivity requirements)
- **Missing syndrome measurement:** Explaining the code structure but not how syndrome extraction works in practice

### Quality Gates Exercised
- Citation coverage (Gate 2) — Steane 1996, Fowler 2012 required
- Code validity (Gate 3) — Steane encoding circuit in Qiskit
- Hardware accuracy (Gate 4) — physical qubit overhead for FTQC
- Track alignment (Gate 5) — Advanced; full stabilizer formalism expected
- Deliverable completeness (Gate 6)

---

## Scenario 6: Research Level — Shor's Algorithm Feasibility Assessment

### User Profile
- **Background:** Graduate student in cryptography, knows number theory and modular arithmetic, wants to understand quantum threat to RSA
- **Goal:** Understand Shor's algorithm structure, estimate hardware requirements for RSA-2048, assess current timeline
- **Platform:** Research understanding only
- **Time:** Research commitment

### User Input
> "I'm a cryptography PhD student. I need to understand Shor's algorithm at a circuit level — how the quantum Fourier transform and modular exponentiation are combined, and what hardware would actually be required to break RSA-2048. What's the realistic timeline, and what's the current state of quantum hardware relative to this threat?"

### Expected Sub-skill Invocation Sequence
1. **sub-profile-intake** — Advanced (cryptography PhD, strong math); goal = Shor's + hardware assessment; platform-agnostic (research focus)
2. **sub-concept-tutor** — Module 6 (Advanced): QFT circuit, phase estimation as QPE, Shor's algorithm structure; modular exponentiation as a quantum oracle; period finding reduction to factoring
3. **sub-circuit-designer** — Shor's circuit structure (for small example: N=15); QFT ASCII circuit for 4 qubits; resource estimates for RSA-2048
4. **sub-hardware-advisor** — Current hardware landscape vs. RSA-2048 requirements; realistic timeline assessment

### Expected Outputs

**Algorithm Structure:**
- Shor's algorithm = quantum period finding + classical modular arithmetic reduction
- Circuit structure: input register (n = log₂N qubits) + output register (n qubits) + modular exponentiation oracle
- QFT applied to input register after oracle; measures period r of f(x) = aˣ mod N
- RSA-2048: N = 2048-bit number; requires n = 2048 qubits in each register = ~4096 logical qubits total

**Resource Estimate for RSA-2048:**

```
Logical qubit requirement:   ~4,000-6,000 logical qubits
Physical qubit requirement:  ~4,000,000 physical qubits (assuming surface code, d=27, 1000:1 overhead)
Gate count:                  ~10^12 T-gates (dominant cost: modular exponentiation)
Computation time:            ~hours per factoring run (with 1M+ physical qubits at MHz gate rates)
Circuit depth:               ~10^10 logical gates

Current best hardware (2025-2026):
  IBM Condor:     1121 physical qubits (no error correction; NISQ only)
  IBM Heron r2:   133 physical qubits (leading superconducting)
  Quantinuum H2:  56 physical qubits (highest fidelity; best for small QEC demonstrations)
  
Gap to RSA-2048:  ~4,000,000 physical qubits needed vs ~1,000 best today
                  = 4 orders of magnitude gap in qubit count + unknown quality at scale

Realistic timeline: 10-20+ years (current consensus: NIST PQC standard published 2024 in anticipation)
```

**QFT ASCII Circuit (4-qubit, as illustration):**
```
q0: ─[H]─[R2]────[R3]──────[R4]──────────────────────────────[SWAP]─
           │      │         │                                  │
q1: ───────●──[H]─│──[R2]───│──[R3]─────────────────[SWAP]───│─────
                  │  │      │  │                    │          │
q2: ──────────────●──●───[H]─│──[R2]──────[SWAP]───│──────────│─────
                             │  │          │        │          │
q3: ─────────────────────────●──●──[H]────│─────────│──────────●─────
                                          └─────────┘
```
(Rk = controlled phase rotation by 2π/2^k)

### Pass Criteria
- [ ] Shor's algorithm decomposed into QPE + classical modular reduction + QFT (all three components named and explained)
- [ ] Modular exponentiation oracle described as the quantum circuit bottleneck (exponentially expensive)
- [ ] RSA-2048 physical qubit requirement stated: ~4M qubits (Gidney & Ekera 2021 estimate: 20M, conservative 4M with aggressive optimization)
- [ ] Current hardware gap explicitly quantified (4 orders of magnitude)
- [ ] NIST PQC standards mentioned as the cryptographic response already in deployment
- [ ] Realistic timeline 10-20+ years based on current roadmaps (IBM 2033 target for error-corrected computation)
- [ ] QFT ASCII circuit is correct for 4 qubits (H, controlled Rk gates, SWAP for bit reversal)
- [ ] Citation to Shor (1994), Gidney & Ekera (2021) for resource estimation

### Common Failure Modes
- **Understating the resource requirement:** Saying "thousands of qubits" when peer-reviewed estimates say millions
- **Overstating the timeline:** Claiming RSA is breakable "soon" — this would be technically inaccurate and alarmist without basis
- **Missing the QFT as a subroutine:** Shor's without explaining QFT's role is incomplete
- **Not citing Gidney & Ekera:** The 2021 Nature paper on RSA-2048 resource estimates is the authoritative reference

### Quality Gates Exercised
- Citation coverage (Gate 2) — Shor 1994, Gidney & Ekera 2021 required
- Code validity (Gate 3) — QFT Qiskit code
- Hardware accuracy (Gate 4) — current qubit counts and 4M physical qubit estimate
- Track alignment (Gate 5) — Advanced; full algorithm structure expected
- Deliverable completeness (Gate 6)
- Graceful degradation (Gate 7) — if WebSearch unavailable, resource estimates from SECOND-KNOWLEDGE-BRAIN.md are acceptable but must be flagged

---

## Test Scenario Summary

| # | User Type | Track | Primary Sub-skills | Key Assertion | Pass/Fail Status |
|---|-----------|-------|-------------------|---------------|-----------------|
| 1 | Python developer, zero QM | Beginner | intake + tutor M1-2 + designer (Bell) + hardware | Bell state circuit in Qiskit + IBM free tier | PENDING |
| 2 | Physics undergrad | Intermediate | intake + tutor M5 (brief) + designer (Grover 3q) + hardware | Correct Grover oracle for \|101⟩, n=2 iterations | PENDING |
| 3 | ML researcher, 50q VQE | Intermediate | intake + tutor (VQE brief) + designer (QAOA sketch) + hardware | IBM Eagle recommendation with SWAP analysis | PENDING |
| 4 | Circuit depth optimization | Intermediate | intake + designer (optimization) + hardware | 6 optimization techniques, Qiskit + TKET code | PENDING |
| 5 | PhD student, Steane code | Advanced | intake + tutor M7 (QEC) + designer (Steane circuit) + hardware | Correct 7-qubit encoding, surface code comparison | PENDING |
| 6 | Cryptography PhD, Shor's | Advanced | intake + tutor M6 (QFT/Shor) + designer (QFT circuit) + hardware | 4M physical qubit estimate, 10-20yr timeline | PENDING |
