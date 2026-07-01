---
name: quantum-circuit-design-assistant/sub-hardware-advisor
description: Compare quantum hardware platforms for the user's specific circuit and goal; provide scored comparison table, recommendation with justification, cloud access guide, and error mitigation strategies
---

## Purpose

Recommend the most appropriate quantum hardware platform for the user's specific use case, circuit specifications, and learning goals. The quantum hardware landscape is diverse — five major physical paradigms, dozens of cloud-accessible devices, and rapidly evolving performance metrics. This sub-skill provides a structured, evidence-based comparison so the user can make an informed choice rather than defaulting to the most-marketed option.

All platform specifications must be cited from official platform documentation or peer-reviewed benchmarking papers. Stale data (> 12 months) is flagged. If WebSearch is available, query for the latest benchmark results before producing the comparison table.

---

## Inputs

- Learner profile (background, experience level, goal)
- Circuit specifications (qubit count, circuit depth, gate types required, algorithm class)
- Budget constraints: free tier / academic access / commercial paid
- Use case: learning and experimentation / research and publications / production / benchmarking / algorithm development
- Specific algorithm class (if known): variational (VQE/QAOA), combinatorial optimization, quantum chemistry, quantum ML, cryptography benchmarking, quantum simulation

---

## Workflow

### Step 1: Verify Current Hardware Specs

If WebSearch is available:
- Search: "IBM Quantum hardware 2025 gate fidelity" or "IBM Heron qubit count fidelity 2025"
- Search: "IonQ Forte specs 2025 algorithmic qubits"
- Search: "Quantinuum H2 specs 2025 gate fidelity"
- Search: "Google Willow quantum supremacy 2024"
- Retrieve up-to-date qubit counts, gate fidelities, and coherence times from official sources

If WebSearch is unavailable:
- Use the platform data in SECOND-KNOWLEDGE-BRAIN.md
- Flag: "Hardware specs sourced from cached knowledge base. Quantum hardware evolves rapidly — verify current specifications at platform websites before making production decisions."

---

### Step 2: Score the Circuit Against Platform Requirements

For the user's specific circuit (if circuit was designed in sub-circuit-designer), check:

| Requirement | Assessment |
|-------------|-----------|
| Qubit count | Does the platform have sufficient qubits for the circuit? |
| Connectivity | Does the platform topology support the circuit's 2-qubit gate pattern without excessive SWAP overhead? |
| Native gate set | Does the circuit's gate set match the platform's native gates, or will expensive decompositions be needed? |
| Circuit depth vs. T2 | Is the circuit depth feasible within the platform's decoherence time budget? |
| Algorithm class fit | Is this platform optimized for this type of algorithm? |

---

### Step 3: Platform Comparison Table

Score each platform on 6 dimensions (1 = poor, 5 = excellent) for the user's specific use case.

**Platform Database (as of 2025/early 2026 — verify with WebSearch):**

---

#### IBM Quantum (Superconducting — Eagle R3, Heron r2)

| Attribute | Value |
|-----------|-------|
| Technology | Superconducting transmon qubits |
| Available systems | IBM Eagle R3 (127 qubits), IBM Heron r2 (133 qubits), IBM Condor (1121 qubits — limited access) |
| Topology | Heavy-hex lattice (limited connectivity — each qubit connects to 2-3 neighbors) |
| Native gates | CX (Eagle), CZ / ECR gate (Heron) |
| Single-qubit fidelity | > 99.9% (Heron) |
| Two-qubit (CX) fidelity | 99.0-99.6% (Heron, device-dependent) |
| T1 (energy relaxation) | 200-500 µs |
| T2 (dephasing) | 100-300 µs |
| Quantum Volume | 512+ (Heron) |
| Access | IBM Quantum Platform: free tier (127 qubits, queue), paid (Heron, priority) |
| Ecosystem | Qiskit — largest open-source quantum ecosystem; excellent documentation; Qiskit Runtime for noise mitigation |
| Best for | Learning, Qiskit development, general NISQ algorithms, variational algorithms on moderate qubit counts |
| Limitations | Heavy-hex connectivity requires significant SWAP overhead for all-to-all connected algorithms |
| Official URL | https://quantum.ibm.com |

---

#### Google Quantum AI (Superconducting — Willow)

| Attribute | Value |
|-----------|-------|
| Technology | Superconducting transmon qubits |
| Available systems | Sycamore (53 qubits, research), Willow (105 qubits, 2024) |
| Topology | 2D grid (each qubit connects to 4 neighbors) |
| Native gates | CZ, iSWAP, Sqrt-iSWAP, Phased X |
| Single-qubit fidelity | > 99.9% |
| Two-qubit fidelity | 99.7% (Willow — below threshold for surface codes) |
| T1 / T2 | ~100-200 µs |
| Benchmarking | Cross-entropy benchmarking (XEB) |
| Access | Research partnerships only; Cirq is open-source for simulation |
| Ecosystem | Cirq — Google's framework; smaller community than Qiskit but excellent for Google hardware-specific work |
| Best for | Academic research; quantum error correction benchmarking; breakthrough algorithm demonstrations |
| Limitations | Not publicly accessible — requires research partnership; Cirq has smaller ecosystem than Qiskit |
| Official URL | https://quantumai.google |

---

#### IonQ (Trapped Ion — Aria, Forte)

| Attribute | Value |
|-----------|-------|
| Technology | Trapped ytterbium ions (¹⁷¹Yb⁺) |
| Available systems | IonQ Aria (25 AQ), IonQ Forte (35 AQ, 36 physical qubits) |
| Topology | All-to-all connectivity (any qubit can interact with any other) |
| Native gates | XX (Mølmer-Sørensen), GPI (single-qubit rotation) |
| Single-qubit fidelity | > 99.9% |
| Two-qubit (XX) fidelity | 99.0-99.9% |
| T1 / T2 | Seconds to minutes (vastly longer than superconducting) |
| Algorithmic Qubits (AQ) | Aria: AQ25; Forte: AQ35 |
| Access | IonQ Cloud; AWS Braket; Azure Quantum; subscription pricing |
| Ecosystem | Supports Qiskit (via IonQ Qiskit provider), Cirq, PennyLane, Braket SDK |
| Best for | Deep circuits (benefits from long T2); all-to-all connectivity algorithms; circuits requiring many 2-qubit gates between non-adjacent qubits |
| Limitations | Gate speed slower than superconducting (~ms vs µs for 2Q gates); fewer total qubits than IBM Eagle |
| Official URL | https://ionq.com |

---

#### Quantinuum (Trapped Ion — H-series)

| Attribute | Value |
|-----------|-------|
| Technology | Trapped ytterbium ions (same physics as IonQ) |
| Available systems | H1 (20 qubits), H2 (56 qubits) |
| Topology | All-to-all (QCCD — Quantum Charge-Coupled Device architecture) |
| Native gates | ZZ gate, single-qubit rotations |
| Single-qubit fidelity | > 99.99% |
| Two-qubit fidelity | > 99.9% (best demonstrated fidelity in the industry as of 2024) |
| Coherence time | Seconds (trapped ion) |
| Quantum Volume | 65536+ (H1) — highest demonstrated QV |
| Access | Subscription (H-series hardware time); TKET compiler (free open-source) |
| Ecosystem | TKET (open-source compiler); supports Qiskit, Cirq, PennyLane via pytket plugins |
| Best for | High-fidelity algorithms; error correction demonstrations; deep circuits that would fail on NISQ superconducting hardware; maximum circuit fidelity regardless of cost |
| Limitations | Highest cost; smaller total qubit count than IBM (56 vs 127+) |
| Official URL | https://www.quantinuum.com |

---

#### Rigetti (Superconducting — Ankaa-2)

| Attribute | Value |
|-----------|-------|
| Technology | Superconducting transmon qubits |
| Available systems | Ankaa-2 (84 qubits) |
| Topology | Octagonal lattice (denser than IBM heavy-hex) |
| Native gates | CZ, Rx, Ry |
| Two-qubit fidelity | ~98-99% (device-dependent) |
| Access | AWS Braket; Rigetti QCS (Quantum Cloud Services) |
| Ecosystem | Pyquil (Rigetti's SDK); Braket SDK |
| Best for | Research with octagonal connectivity; AWS Braket ecosystem integration |
| Limitations | Smaller ecosystem than IBM; typically trailing IBM and trapped-ion in fidelity |
| Official URL | https://www.rigetti.com |

---

#### D-Wave (Quantum Annealing — Advantage2)

| Attribute | Value |
|-----------|-------|
| Technology | Quantum annealing — NOT gate-based quantum computing |
| Available systems | D-Wave Advantage2 (5000+ qubits, Pegasus topology) |
| Paradigm | QUBO (Quadratic Unconstrained Binary Optimization) / Ising model |
| Access | D-Wave Leap (free cloud access for development); Braket |
| Best for | Combinatorial optimization, sampling, logistics problems expressed as QUBO |
| Limitations | NOT suitable for gate-based algorithms (Grover's, Shor's, QFT); fundamentally different paradigm — not "general quantum computing" |
| Official URL | https://www.dwavesys.com |
| Important note | D-Wave is often misunderstood as general quantum computing; it is specialized for optimization problems in the Ising/QUBO formulation only |

---

#### PsiQuantum (Photonic — Pre-commercial)

| Attribute | Value |
|-----------|-------|
| Technology | Photonic qubits (linear optical quantum computing) |
| Status | Not yet commercially available (targeting fault-tolerant QC at scale) |
| Target | 1 million+ physical qubits for fault-tolerant operations |
| Access | Research partnerships only |
| Best for | Future FTQC applications; not a current option for circuit design learners |

---

### Step 4: Produce Scored Comparison Table

Score each relevant platform (exclude D-Wave unless user's goal is optimization, exclude PsiQuantum unless user explicitly asks about future platforms) on the following dimensions:

**Scoring Dimensions:**
- **Qubit count vs. need** (1-5): Does it have enough qubits for the user's circuit + overhead?
- **Gate fidelity** (1-5): Higher two-qubit fidelity = better circuit success probability
- **Connectivity** (1-5): Does the topology match the circuit's connectivity needs?
- **Ecosystem maturity** (1-5): Quality of SDK, documentation, tutorials, community
- **Access cost** (1-5): 5 = free; 1 = expensive subscription
- **Algorithm fit** (1-5): Is this platform known for the user's algorithm class?

**Example table for a learner who wants to implement Grover's algorithm with 4 qubits, Qiskit preferred, free tier required:**

| Platform | Qubits (vs need) | Fidelity | Connectivity | Ecosystem | Access Cost | Algorithm Fit | Total |
|----------|-----------------|---------|-------------|-----------|------------|---------------|-------|
| IBM Quantum (Eagle) | 5 (127 >> 4) | 4 | 3 (heavy-hex, 4q OK) | 5 (Qiskit) | 5 (free tier) | 4 | 26/30 |
| IonQ Aria | 5 (25 >> 4) | 4 | 5 (all-to-all) | 3 (Qiskit via provider) | 2 (paid) | 4 | 23/30 |
| Quantinuum H2 | 5 (56 >> 4) | 5 | 5 (all-to-all) | 3 (TKET) | 1 (most expensive) | 5 | 24/30 |
| Rigetti Ankaa-2 | 5 (84 >> 4) | 3 | 4 (octagonal) | 2 (Pyquil) | 3 (Braket fees) | 3 | 20/30 |

**Recommendation: IBM Quantum** — free tier, Qiskit ecosystem, more than sufficient qubits for a 4-qubit Grover's circuit, and heavy-hex connectivity is adequate for this small circuit size.

---

### Step 5: Cloud Access Guide

Provide a step-by-step guide for accessing the recommended platform.

**IBM Quantum (Recommended for most learners):**
1. Visit https://quantum.ibm.com and create a free account (IBM ID)
2. Navigate to the IBM Quantum Platform dashboard
3. Copy your API key from Account Settings
4. Install Qiskit and IBM provider: `pip install qiskit qiskit-ibm-runtime qiskit-aer`
5. Authenticate in Python:
   ```python
   from qiskit_ibm_runtime import QiskitRuntimeService
   QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_API_KEY")
   service = QiskitRuntimeService()
   backend = service.least_busy(min_num_qubits=5, simulator=False)
   print(f"Running on: {backend.name}")
   ```
6. Submit a circuit using SamplerV2 (Qiskit Runtime):
   ```python
   from qiskit_ibm_runtime import SamplerV2 as Sampler
   from qiskit import transpile
   from qiskit import QuantumCircuit

   qc = QuantumCircuit(2, 2)
   qc.h(0); qc.cx(0, 1); qc.measure_all()
   transpiled = transpile(qc, backend=backend, optimization_level=3)
   sampler = Sampler(backend)
   job = sampler.run([transpiled])
   result = job.result()
   print(result[0].data.meas.get_counts())
   ```
7. Monitor job status in IBM Quantum Platform dashboard or via `job.status()`

**IonQ via AWS Braket:**
1. Create an AWS account and enable Braket service (AWS console)
2. Install: `pip install amazon-braket-sdk`
3. Access IonQ hardware:
   ```python
   from braket.aws import AwsDevice
   device = AwsDevice("arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1")
   # Convert Qiskit circuit via qiskit-braket-provider:
   # pip install qiskit-braket-provider
   from qiskit_braket_provider import BraketProvider
   provider = BraketProvider()
   backend = provider.get_backend("IonQ Device: Aria 1")
   ```
4. Note: Braket charges per-task and per-shot; estimate costs before running

**Quantinuum via Qiskit (pytket):**
1. Register at https://um.qapi.quantinuum.com
2. Install: `pip install pytket pytket-quantinuum`
3. Access H-series:
   ```python
   from pytket.extensions.quantinuum import QuantinuumBackend
   backend = QuantinuumBackend("H1-1", machine_debug=False)
   backend.login()
   ```

---

### Step 6: Error Mitigation Recommendations

For the recommended platform, specify the most effective noise mitigation strategies.

**For IBM Quantum (Superconducting):**
- **Zero-Noise Extrapolation (ZNE):** Available in Qiskit Runtime Estimator; run at noise scales [1, 2, 3] and extrapolate to zero. Best for circuits with ≤ 50 gates.
- **Dynamical Decoupling (DD):** `DynamicalDecoupling` transpiler pass in Qiskit; inserts X-X pulses on idle qubits. Free, significant improvement for circuits with wait times.
- **M3 Measurement Mitigation:** `mthree` package from IBM; calibrates and corrects readout errors. Run once per day per backend.
- **Optimization level 3 transpilation:** `transpile(qc, backend, optimization_level=3)` — noise-aware gate synthesis.

**For IonQ / Quantinuum (Trapped Ion):**
- **Longer T2 = deeper circuits feasible:** Most NISQ mitigation techniques are less critical here; focus on native gate decomposition.
- **Debiasing (IonQ-specific):** IonQ's proprietary technique that averages over random circuit variations to reduce systematic errors.
- **Symmetry verification:** For algorithms with known output symmetries (e.g., Grover's should give low probability for non-target states), post-select on physically valid results.

**For all platforms:**
- **Simulator validation first:** Always test on AerSimulator (noiseless, then with noise model) before submitting to real hardware.
- **Shot count:** 1024-8192 shots per circuit for reliable statistics; fewer for expensive hardware time.
- **Circuit cutting (for large circuits):** For circuits exceeding hardware qubit count, use Qiskit's `CircuitKnitting` toolbox to cut into smaller subcircuits.

---

## Outputs

1. **Platform Comparison Table:** All relevant platforms scored on 6 dimensions for the user's specific use case
2. **Recommended Platform:** Single recommendation with justification (2-3 sentences explaining why this platform scores highest for this specific user)
3. **Why Not X:** Brief notes on why non-recommended platforms were not chosen (helps the user understand the trade-offs)
4. **Cloud Access Guide:** Step-by-step instructions for the recommended platform (code included)
5. **Error Mitigation Strategy:** 2-3 specific techniques for the recommended platform with implementation notes
6. **Cost Estimate:** Rough estimate of compute cost if applicable (e.g., "IBM free tier: 10 minutes/month; Braket IonQ: ~$0.01-$0.10 per task + $0.00035 per shot")

---

## Quality Gate

This sub-skill's output is accepted when:

1. At least 3 platforms are compared in the scoring table (unless the user explicitly requested only one platform)
2. All platform specs (qubit count, gate fidelity, T1/T2) are cited from official documentation or peer-reviewed papers published within 12 months; stale or unverifiable data is explicitly flagged with a date
3. If WebSearch was available, it was used to verify current platform specifications before producing the table
4. A single recommended platform is identified with a clear justification referencing the user's specific circuit and goal
5. The cloud access guide includes working code for authenticating and submitting a circuit to the recommended platform
6. D-Wave is only recommended if the user's goal is explicitly combinatorial optimization in QUBO form; otherwise, its fundamentally different paradigm is noted with the caveat that it is not general-purpose quantum computing
7. Error mitigation recommendations are platform-specific (not generic); at least 2 techniques are named with implementation steps
