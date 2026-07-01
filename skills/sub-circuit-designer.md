---
name: quantum-circuit-design-assistant/sub-circuit-designer
description: Translate algorithm descriptions into gate sequences, ASCII circuit diagrams, and complete Qiskit code; analyze circuit metrics and recommend optimizations for NISQ hardware
---

## Purpose

Convert a user's algorithm description or circuit goal into a professionally structured quantum circuit deliverable: an ASCII diagram, complete runnable Qiskit code, circuit metrics analysis, hardware connectivity validation, and prioritized optimization recommendations. This sub-skill ensures the learner not only gets a working circuit but understands *why* each gate is placed, how to read circuit depth and gate counts, and what constraints the target hardware imposes.

---

## Inputs

- Algorithm description or circuit goal (e.g., "Create a 3-qubit GHZ state", "Implement Deutsch-Jozsa for f:{0,1}² → {0,1}", "Build a variational quantum eigensolver ansatz with 4 qubits and 2 layers")
- Target hardware platform (optional — used for connectivity validation and transpilation notes)
- Optimization goal: minimize depth / minimize gate count / minimize CNOT count / no preference
- Learner track (Beginner/Intermediate/Advanced) — determines how much the explanation scaffolds vs. assumes

---

## Workflow

### Step 1: Algorithm Clarification (if needed)

If the algorithm description is ambiguous or underspecified, ask exactly one clarifying question before proceeding:
- "How many qubits should the circuit use?"
- "Which specific version of this algorithm do you need (e.g., Grover's with which oracle)?"
- "Do you want the full algorithm or a specific subroutine (e.g., just the QFT, not the full phase estimation)?"

If the description is clear, skip this step.

---

### Step 2: Gate Sequence Decomposition

Break the algorithm into a gate sequence, step by step, in order of application (left to right in circuit notation).

For each gate, specify:
- Gate type (H, X, Y, Z, S, T, CNOT/CX, CZ, SWAP, Toffoli/CCX, Rx, Ry, Rz, or custom controlled gate)
- Target qubit(s) and control qubit(s) if applicable
- Brief purpose (e.g., "creates superposition", "entangles q0 and q1", "implements phase kickback")

Present the sequence as a numbered table:

| Step | Gate | Qubit(s) | Purpose |
|------|------|---------|---------|
| 1 | H | q0 | Creates superposition on control qubit |
| 2 | CX | control=q0, target=q1 | Entangles q0 and q1 |
| ... | ... | ... | ... |

---

### Step 3: ASCII Circuit Diagram

Draw the circuit diagram using the standardized ASCII format used in this skill.

**Format rules:**
- One horizontal line per qubit, labeled `q0:`, `q1:`, etc.
- Classical bits (for measurement) labeled `c0:`, `c1:`, etc.
- Gates shown as `[X]`, `[H]`, `[Rz]`, `[CX]` etc. inside brackets
- `■` marks a control qubit; `╳` marks a SWAP; `M` or `[M]` marks measurement
- Vertical connections (│) link multi-qubit gates
- Barriers shown as `┆` (optional, for clarity)

**Examples:**

Bell state circuit:
```
     ┌───┐      ┌─┐
q0: ─┤ H ├──────■──┤M├─
     └───┘      │  └─┘
               ┌┴┐ ┌─┐
q1: ───────────┤X├─┤M├─
               └─┘ └─┘
c0: ═══════════════════╗
c1: ══════════════════╗╝
```

Simplified ASCII (acceptable for deep circuits):
```
q0: ─[H]─────■─────[M]─
             │
q1: ─────────X─────[M]─
```

3-qubit GHZ state:
```
q0: ─[H]─■─────────[M]─
          │
q1: ──────X──■──────[M]─
             │
q2: ─────────X──────[M]─
```

Grover's oracle (marking |11⟩):
```
q0: ─[H]─■──[H]─[X]─■──[X]─[H]─[M]─
          │           │
q1: ─[H]─■──[H]─[X]─■──[X]─[H]─[M]─
     Init  Oracle   Diffusion
```

---

### Step 4: Qiskit Code

Write complete, runnable Qiskit 1.x code implementing the circuit.

**Mandatory code structure:**
```python
# === IMPORTS ===
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram  # optional, for notebook use

# === CIRCUIT CONSTRUCTION ===
# [Describe what algorithm this circuit implements]
n_qubits = X
n_classical = Y
qc = QuantumCircuit(n_qubits, n_classical)

# [Gate-by-gate construction with inline comments]
qc.h(0)        # Apply Hadamard to qubit 0 — creates superposition
qc.cx(0, 1)    # CNOT: q0 control, q1 target — entangles qubits

# === MEASUREMENT ===
qc.measure(range(n_qubits), range(n_classical))  # or qc.measure_all()

# === SIMULATION ===
simulator = AerSimulator()
# Optional: specify method for statevector or density matrix
# simulator = AerSimulator(method='statevector')  # for state inspection

compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

print("Circuit results (1024 shots):")
print(counts)

# === CIRCUIT VISUALIZATION ===
print("\nCircuit diagram:")
print(qc.draw(output='text'))

# === CIRCUIT METRICS ===
from qiskit.circuit.library import HGate, CXGate
depth = qc.depth()
gate_counts = dict(qc.count_ops())
print(f"\nCircuit depth: {depth}")
print(f"Gate counts: {gate_counts}")
```

**Platform-specific variants (add as comments):**
- For IBM Quantum cloud: replace `AerSimulator()` with IBM Runtime `SamplerV2` via `QiskitRuntimeService`
- For Google Cirq: provide equivalent gate sequence as a code comment
- For IonQ/Braket: note which native gates differ (e.g., IonQ uses XX/YY gates, not CNOT directly)

---

#### Reference Implementations

**Bell State (2 qubits):**
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
qc.h(0)         # Hadamard on qubit 0: |0> -> (|0>+|1>)/sqrt(2)
qc.cx(0, 1)     # CNOT: entangles qubits -> (|00>+|11>)/sqrt(2) = |Phi+>
qc.measure([0, 1], [0, 1])

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1000).result()
print(result.get_counts())  # Expect: {'00': ~500, '11': ~500}
print(qc.draw('text'))
```

**Grover's Search (3 qubits, target |101>):**
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

n = 3  # 3 qubits, 8 states
target = '101'  # target state to find

qc = QuantumCircuit(n, n)

# Initialization: uniform superposition
qc.h(range(n))
qc.barrier()

# Grover iterations: optimal = floor(pi/4 * sqrt(N)) = floor(pi/4 * sqrt(8)) ≈ 2
n_iterations = int(np.pi / 4 * np.sqrt(2**n))

for _ in range(n_iterations):
    # Oracle for |101>: marks target with -1 phase
    # |101>: q0=1, q1=0, q2=1 -> apply X to q1 (to flip 0->1), CZ on all, X to q1
    qc.x(1)                # flip q1 so oracle sees |111>
    qc.h(2)                # change basis for CCX acting as phase flip via ancilla trick
    qc.ccx(0, 1, 2)        # Toffoli: flips q2 if q0=1 AND q1=1 (after X on q1)
    qc.h(2)                # undo basis change
    qc.x(1)                # undo X on q1
    qc.barrier(label='Oracle')

    # Diffusion operator (inversion about average)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.ccx(0, 1, 2)        # n-controlled Z via HCCXHon last qubit
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))
    qc.barrier(label='Diffusion')

qc.measure(range(n), range(n))

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=2048).result()
counts = result.get_counts()
print(f"Grover results (target=|{target}>):")
print(sorted(counts.items(), key=lambda x: -x[1])[:5])
print(qc.draw('text'))
```

**Quantum Fourier Transform (3 qubits):**
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

def qft_circuit(n: int) -> QuantumCircuit:
    """Build n-qubit QFT circuit (without final SWAP reordering)."""
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            # Controlled-Rz(2pi/2^(k-j+1)) gate
            angle = 2 * np.pi / (2 ** (k - j + 1))
            qc.cp(angle, k, j)  # Controlled phase gate
        qc.barrier()
    # Reverse qubit order (standard QFT output convention)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    return qc

n = 3
qft = qft_circuit(n)
qft_with_measure = qft.copy()
qft_with_measure.measure_all()

sim = AerSimulator()
result = sim.run(transpile(qft_with_measure, sim), shots=1024).result()
print("QFT on |000> (should give uniform distribution):")
print(result.get_counts())
print(qft.draw('text'))
```

---

### Step 5: Circuit Metrics Analysis

Compute and report:

| Metric | How to Compute | Why It Matters |
|--------|---------------|----------------|
| Circuit depth | `qc.depth()` | Limits execution on NISQ hardware (must fit within T2 time budget) |
| Total gate count | `sum(qc.count_ops().values())` | Total time on device; more gates = more noise |
| Single-qubit gates | Count from `qc.count_ops()` | Cheap on most platforms |
| Two-qubit gates (CX/CZ) | Count CX, CZ, etc. from ops | Most expensive; dominant noise source on superconducting hardware |
| T-gate count | Count T, Tdg from ops | Critical for fault-tolerant resource estimation |
| NISQ classification | Compare depth to hardware T2/gate_time | Determines if circuit is feasible on NISQ hardware |

**NISQ classification thresholds (approximate, varies by platform):**
- **NISQ-feasible:** depth ≤ 100, ≤ 50 qubits, ≤ 30 two-qubit gates (superconducting); adjust for trapped ion (deeper circuits feasible due to longer T2)
- **NISQ-challenging:** depth 100-500; requires noise mitigation techniques (ZNE, DD, PEC)
- **FTQC-required:** depth > 500 without error correction, logical qubit algorithms, or T-gate counts in thousands

**Example metrics table:**
```
CIRCUIT METRICS
===============
Circuit Name:       Bell State
Qubits:             2
Circuit Depth:      2
Total Gates:        3 (H: 1, CX: 1, Measure: 2, barrier not counted)
Single-qubit Gates: 1
Two-qubit Gates:    1 (CX)
T-gate Count:       0
NISQ Classification: NISQ-feasible (trivially — depth 2, 2 qubits)
```

---

### Step 6: Hardware Connectivity Validation

If a target hardware platform is specified, check the circuit's gate operations against the platform's native gate set and qubit connectivity.

**Common connectivity constraints:**

| Platform | Topology | Native 2Q Gate |
|----------|----------|---------------|
| IBM Eagle R3 (127q) | Heavy-hex lattice (limited connectivity) | CX (CNOT) |
| IBM Heron r2 (133q) | Heavy-hex, improved | CZ or ECR gate |
| Google Sycamore (53q) | 2D grid | CZ, iSWAP |
| IonQ Forte (36q) | All-to-all (trapped ion) | XX (Mølmer-Sørensen) |
| Quantinuum H2 (56q) | All-to-all (trapped ion) | ZZ gate |
| Rigetti Ankaa-2 (84q) | Octagonal lattice | CZ |

**Connectivity validation logic:**
1. For each two-qubit gate in the circuit, check if the target qubit pair is adjacent in the hardware graph
2. If not adjacent: flag the gate and note that the transpiler must insert SWAP gates (increases depth by 3 per SWAP)
3. For all-to-all connected platforms (IonQ, Quantinuum): no connectivity issues; flag native gate mismatch instead

**Example validation output:**
```
CONNECTIVITY CHECK: IBM Eagle R3 (heavy-hex lattice)
====================================================
CX(q0, q1): [OK] — q0-q1 is a native edge on IBM Eagle
CX(q2, q5): [OK] — q2-q5 is a native edge
CX(q1, q4): [WARNING] — q1-q4 is NOT adjacent; transpiler will insert 2 SWAP gates
             This increases circuit depth by 6 gates and adds ~0.3% error per SWAP.
             Recommendation: remap to qubits 1-3 to avoid the SWAP overhead.
```

---

### Step 7: Optimization Recommendations

Provide at least 2 concrete optimization recommendations, ordered by impact (highest impact first).

**Optimization Catalog:**

1. **Gate cancellation:** Adjacent inverse gates cancel (e.g., HH = I, XX = I). Identify and remove them.
   - Impact: Reduces total gate count directly
   - Example: "Your circuit has H on q0 at step 3 and H on q0 at step 4 — they cancel to identity; remove both."

2. **Commutation rules:** Gates on non-overlapping qubits can be reordered to enable further cancellations.
   - Example: "Z on q0 (step 5) and H on q1 (step 5) can be parallelized — reduces circuit depth by 1."

3. **CNOT reduction via SWAP reordering:** Re-mapping qubits to minimize CNOT/SWAP insertion by the transpiler.
   - Impact: Reduces 2-qubit gate count (the dominant noise source)

4. **Transpiler optimization level:** Use `transpile(qc, backend, optimization_level=3)` for maximum compression.
   - Note: Level 3 uses noise-aware synthesis (slow for large circuits, best for ≤ 20 qubits)

5. **TKET compiler:** For circuits > 20 qubits on NISQ hardware, TKET (from Quantinuum) often achieves better compression than Qiskit's transpiler.

6. **Decompose Toffoli:** CCX (Toffoli) costs 6 CNOT gates in standard decomposition; can be reduced to 3 CNOTs with 8 single-qubit gates if one control is measured immediately after.

7. **Parameterized circuits for VQE/QAOA:** Use `ParameterVector` in Qiskit for variational circuits — avoids rebuilding circuits on every optimization step.

8. **Dynamical decoupling (DD):** For idle qubits, insert X-X or XYXY pulse sequences to combat dephasing (T2 error). Available via Qiskit's `DynamicalDecoupling` transpiler pass.

9. **Gate synthesis for rotation angles:** For Rz(θ) with specific θ (e.g., π/4, π/8), check if the angle decomposes into fewer T-gates using Solovay-Kitaev decomposition.

10. **Measurement error mitigation:** Apply `M3` (Matrix-free Measurement Mitigation) from Qiskit Runtime to correct readout errors without additional circuit overhead.

---

## Outputs

For each circuit design request, produce:

1. **Gate Sequence Table:** Numbered steps with gate type, qubits, and purpose
2. **ASCII Circuit Diagram:** Legible ASCII diagram following the standard format
3. **Complete Qiskit Code:** Runnable Python code including imports, construction, measurement, simulation, and metrics
4. **Circuit Metrics Table:** Depth, gate counts, NISQ classification
5. **Hardware Connectivity Check:** (if platform specified) Pass/fail per gate, SWAP insertion warnings, qubit remapping suggestions
6. **Optimization Recommendations:** At least 2, ordered by impact, with specific gate locations referenced

---

## Quality Gate

This sub-skill's output is accepted when:

1. The gate sequence is correct and complete for the requested algorithm (no missing steps)
2. The ASCII circuit diagram is readable and consistent with the gate sequence
3. The Qiskit code is syntactically valid (all imports present, Qiskit 1.x API, no deprecated calls), includes at minimum a QuantumCircuit, measurement, and simulation or statevector inspection
4. Circuit metrics table covers all 6 metrics: depth, total gates, single-qubit, two-qubit, T-count, NISQ classification
5. If a target hardware platform was specified, connectivity validation was completed and any SWAP insertions were flagged
6. At least 2 optimization recommendations are provided with specific circuit locations referenced
7. If the circuit is classified FTQC-required, this is explicitly stated with an explanation of why and what FTQC resources would be needed
