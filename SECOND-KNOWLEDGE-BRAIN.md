# SECOND-KNOWLEDGE-BRAIN.md — Quantum Circuit Design Learning Assistant (Skill #245)

> **Self-improving knowledge base.** Updated weekly by `tools/knowledge_updater.py`. Do not manually edit entries in the Knowledge Update Log or Research Papers table — use the updater script to ensure deduplication. The Core Concepts, Frameworks, and Data Sources sections may be manually curated.

---

## 1. Core Concepts & Frameworks

### 1.1 Qubit and Quantum State

A qubit is the fundamental unit of quantum information. Unlike a classical bit (0 or 1), a qubit can exist in a superposition of both states simultaneously.

**Mathematical formulation:**
- State vector: |ψ⟩ = α|0⟩ + β|1⟩, where α, β ∈ ℂ and |α|² + |β|² = 1
- Computational basis states: |0⟩ = [1, 0]ᵀ, |1⟩ = [0, 1]ᵀ
- Bloch sphere representation: any pure single-qubit state maps to a point on the unit sphere
  - |0⟩ → north pole (θ=0)
  - |1⟩ → south pole (θ=π)
  - |+⟩ = (|0⟩+|1⟩)/√2 → positive x-axis (θ=π/2, φ=0)
  - |−⟩ = (|0⟩−|1⟩)/√2 → negative x-axis (θ=π/2, φ=π)
  - |i⟩ = (|0⟩+i|1⟩)/√2 → positive y-axis

**Source:** Nielsen & Chuang, Chapter 1 (ISBN 978-1107002173)

---

### 1.2 Quantum Gates

Quantum gates are unitary matrices that transform qubit states. Unlike classical logic gates, all quantum gates are reversible.

**Single-qubit gates:**

| Gate | Symbol | Matrix | Effect |
|------|--------|--------|--------|
| Pauli-X (NOT) | X | [[0,1],[1,0]] | Bit flip: |0⟩↔|1⟩ |
| Pauli-Y | Y | [[0,-i],[i,0]] | Bit+phase flip |
| Pauli-Z | Z | [[1,0],[0,-1]] | Phase flip: |1⟩ → -|1⟩ |
| Hadamard | H | [[1,1],[1,-1]]/√2 | Creates superposition: |0⟩ → |+⟩ |
| Phase (S) | S | [[1,0],[0,i]] | π/2 phase rotation |
| T gate | T | [[1,0],[0,e^(iπ/4)]] | π/4 phase; expensive in fault-tolerant QC |
| Rx(θ) | Rx | e^(-iθX/2) | Rotation around x-axis by θ |
| Ry(θ) | Ry | e^(-iθY/2) | Rotation around y-axis by θ |
| Rz(θ) | Rz | e^(-iθZ/2) | Rotation around z-axis by θ |

**Two-qubit gates:**

| Gate | Qubits | Effect |
|------|--------|--------|
| CNOT (CX) | control + target | Flips target if control = |1⟩ |
| CZ | control + target | Applies Z to target if control = |1⟩ |
| SWAP | 2 qubits | Exchanges state of two qubits |
| Toffoli (CCX) | 2 controls + target | Flips target if both controls = |1⟩ (universal classical gate) |
| iSWAP | 2 qubits | Native to some superconducting platforms |

**Source:** Nielsen & Chuang, Chapter 4; Qiskit Textbook, Chapter 1

---

### 1.3 Quantum Circuit Notation

A quantum circuit reads left to right. Each horizontal line is a qubit wire; gates are boxes or symbols on the wires; vertical lines with dots and targets represent controlled operations; meters [M] represent measurement.

**Standard ASCII convention used in this skill:**
```
q0: ─[H]─────────■─────[M]─
                  │
q1: ─────────────X─────[M]─
```
- `■` = control qubit
- `X` on target wire = CNOT target
- `[H]` = Hadamard gate
- `[M]` = measurement

**Source:** IBM Quantum Learning, Circuit Basics module

---

### 1.4 Entanglement and Bell States

Quantum entanglement is a correlation between qubits such that the state of one cannot be described independently of the other. Bell states are the maximally entangled two-qubit states:

| Bell State | Formula | Circuit |
|-----------|---------|---------|
| Φ⁺ | (|00⟩+|11⟩)/√2 | H on q0, CNOT(q0→q1) |
| Φ⁻ | (|00⟩−|11⟩)/√2 | H on q0, Z on q0, CNOT |
| Ψ⁺ | (|01⟩+|10⟩)/√2 | H on q0, CNOT, X on q1 |
| Ψ⁻ | (|01⟩−|10⟩)/√2 | H on q0, CNOT, X on q0 |

GHZ state (3-qubit generalization): (|000⟩+|111⟩)/√2 — requires H on q0, CNOT(q0→q1), CNOT(q0→q2)

**Source:** Nielsen & Chuang, Chapter 2; Bell (1964), Physics 1(3):195-200

---

### 1.5 Quantum Measurement and the Born Rule

Measuring a qubit in the computational basis collapses its superposition:
- P(0) = |α|², P(1) = |β|² for state α|0⟩ + β|1⟩
- Measurement is destructive — the post-measurement state is the eigenstate, not the original superposition
- The Born rule: probability of outcome m is |⟨m|ψ⟩|²

**No-cloning theorem:** It is impossible to create a perfect copy of an arbitrary unknown quantum state. This has profound implications for quantum communication and error correction.

**Source:** Nielsen & Chuang, Chapter 2.2; Wootters & Zurek (1982), Nature 299:802

---

### 1.6 Key Quantum Algorithms

**Deutsch-Jozsa Algorithm (1992)**
- Problem: Determine if a function f:{0,1}ⁿ → {0,1} is constant or balanced using a single quantum query
- Classical: requires 2^(n-1)+1 queries in worst case
- Quantum: 1 query (exponential speedup for the oracle model)
- Source: Deutsch & Jozsa (1992), Proc. R. Soc. Lond. A 439:553-558

**Grover's Search Algorithm (1996)**
- Problem: Find a marked item in an unsorted database of N items
- Classical: O(N) queries
- Quantum: O(√N) queries (quadratic speedup)
- Circuit: Oracle (marks target) + Diffusion operator (amplifies target amplitude), repeated O(√N) times
- Source: Grover (1996), Phys. Rev. Lett. 79:325-328

**Shor's Factoring Algorithm (1994)**
- Problem: Factor a large integer N into prime factors
- Classical: Sub-exponential (best known: GNFS) but exponential in general
- Quantum: Polynomial O((log N)²(log log N)(log log log N)) — exponential speedup
- Requires: Quantum Fourier Transform, modular exponentiation as oracle
- Hardware requirement: ~4000 logical qubits for RSA-2048 (far beyond NISQ era)
- Source: Shor (1994/1997), SIAM J. Comput. 26:1484-1509

**Quantum Phase Estimation (QPE)**
- Foundational subroutine for Shor's and quantum chemistry algorithms
- Estimates eigenphase of a unitary to n-bit precision
- Source: Kitaev (1995), arXiv:quant-ph/9511026

---

### 1.7 Quantum Error Correction

**Why needed:** Real qubits suffer decoherence (T1 = energy relaxation time, T2 = dephasing time), gate errors, and readout errors. Error correction encodes 1 logical qubit in multiple physical qubits.

**Steane [[7,1,3]] Code:**
- 7 physical qubits encode 1 logical qubit
- Can correct any single-qubit error (X, Y, or Z flip)
- Based on classical Hamming code
- Source: Steane (1996), Phys. Rev. Lett. 77:793

**Surface Code:**
- Leading candidate for fault-tolerant quantum computing
- Threshold error rate ~1% (achievable with current superconducting hardware)
- Requires ~1000 physical qubits per logical qubit at practical error rates
- Source: Fowler et al. (2012), Phys. Rev. A 86:032324

**Stabilizer Formalism:**
- Efficient classical description of many error-correcting codes
- Uses Pauli group generators to specify code space
- Source: Gottesman (1997), PhD thesis, Caltech

---

### 1.8 Quantum Advantage Criteria

- **Quantum supremacy/advantage:** A quantum device performing a specific task faster than any classical supercomputer
- **NISQ era:** Noisy Intermediate-Scale Quantum — 50-1000 qubits, no error correction, limited circuit depth
- **Fault-tolerant quantum computing (FTQC):** Uses error-correcting codes; requires ~1M+ physical qubits for practical RSA-cracking
- **Quantum volume (QV):** IBM metric; measures effective qubit count accounting for connectivity and fidelity; log₂(QV) roughly = achievable circuit depth on n qubits
- **Algorithmic Qubits (AQ):** IonQ metric; number of qubits capable of successfully executing a specific benchmark circuit

---

## 2. Key Research Papers

| # | Title | Authors | Year | Venue | DOI/URL | Relevance |
|---|-------|---------|------|-------|---------|-----------|
| 1 | Quantum Computation and Quantum Information (textbook) | Nielsen, Chuang | 2000 | Cambridge UP | ISBN 978-1107002173 | Definitive reference; basis for all concept modules |
| 2 | Algorithms for Quantum Computation: Discrete Logarithms and Factoring | Shor, P.W. | 1994 | FOCS | https://ieeexplore.ieee.org/document/365700 | Shor's algorithm; foundational for advanced track |
| 3 | A fast quantum mechanical algorithm for database search | Grover, L.K. | 1996 | STOC | https://arxiv.org/abs/quant-ph/9605043 | Grover's search algorithm |
| 4 | Rapid solution of problems by quantum computation | Deutsch, D. & Jozsa, R. | 1992 | Proc. R. Soc. A | https://doi.org/10.1098/rspa.1992.0167 | Deutsch-Jozsa; first quantum speedup proof |
| 5 | Quantum error correction via codes over GF(4) | Calderbank et al. | 1998 | IEEE Trans. Inf. Theory | https://arxiv.org/abs/quant-ph/9608006 | CSS codes; basis of Steane code |
| 6 | Surface codes: Towards practical large-scale quantum computation | Fowler et al. | 2012 | Phys. Rev. A | https://arxiv.org/abs/1208.0928 | Surface code — leading FTQC approach |
| 7 | Quantum supremacy using a programmable superconducting processor | Arute et al. (Google) | 2019 | Nature | https://doi.org/10.1038/s41586-019-1666-5 | Google Sycamore quantum supremacy claim |
| 8 | Quantum volume as a benchmark for near-term quantum computing devices | Cross et al. (IBM) | 2019 | Phys. Rev. A | https://arxiv.org/abs/1811.12926 | IBM Quantum Volume metric |
| 9 | Demonstrating quantum advantage with trapped-ion qubits | IonQ | 2022 | Phys. Rev. X Quantum | https://arxiv.org/abs/2107.09238 | IonQ AQ metric and algorithmic benchmarking |
| 10 | Reliable quantum computers | Preskill, J. | 1998 | Proc. R. Soc. A | https://arxiv.org/abs/quant-ph/9705052 | NISQ era concept; threshold theorem |
| 11 | Lecture Notes on Quantum Computation | Preskill, J. | 2022 | Caltech Ph229 | http://theory.caltech.edu/~preskill/ph229/ | Best free advanced curriculum |
| 12 | An error-correcting code | Steane, A. | 1996 | Phys. Rev. Lett. | https://arxiv.org/abs/quant-ph/9601029 | [[7,1,3]] Steane code |
| 13 | A single quantum cannot be cloned | Wootters & Zurek | 1982 | Nature | https://doi.org/10.1038/299802a0 | No-cloning theorem |
| 14 | Quantum teleportation of an unknown quantum state | Bennett et al. | 1993 | Phys. Rev. Lett. | https://arxiv.org/abs/quant-ph/9307004 | Teleportation protocol; Bell state application |
| 15 | Characterizing quantum supremacy in near-term devices | Boixo et al. | 2018 | Nature Physics | https://arxiv.org/abs/1608.00263 | Cross-entropy benchmarking methodology |
| 16 | Qiskit: An Open-source Framework for Quantum Computing | IBM Qiskit contributors | 2019 | Zenodo | https://doi.org/10.5281/zenodo.2562111 | Official Qiskit citation |
| 17 | High-fidelity trapped-ion qubit operations with AI-enabled chaotic optical beams | Kang et al. | 2023 | Nature Physics | https://doi.org/10.1038/s41567-023-02282-2 | Latest trapped-ion fidelity advances |
| 18 | Exponential quantum speed-up over classical simulation via quantum approximate optimization | Farhi et al. | 2014 | arXiv | https://arxiv.org/abs/1411.4028 | QAOA — NISQ-era algorithm |
| 19 | Real-time error correction for quantum computing using deep neural networks | Kim et al. | 2023 | Nature | https://doi.org/10.1038/s41586-023-06438-z | ML-assisted error correction (IBM) |

---

## 3. State-of-the-Art Methods & Tools

### Circuit Design & Simulation
- **Qiskit (IBM):** Most widely used framework; Python SDK; supports real hardware + Aer simulator; Qiskit Runtime for cloud execution
  - Version: 1.x (Terra/Aer unified); install with `pip install qiskit`
  - Key modules: `QuantumCircuit`, `transpile`, `AerSimulator`, `StatevectorSimulator`
- **Cirq (Google):** Python framework for NISQ algorithms; native Sycamore gates; strong for optimization circuits
- **PennyLane (Xanadu):** Differentiable quantum computing; ML integration; supports multiple backends
- **Q# (Microsoft):** High-level domain-specific language; Azure Quantum integration; resource estimation
- **Braket (AWS):** Cloud access to multiple hardware providers (IonQ, Rigetti, Quantinuum) via unified SDK
- **TKET (Quantinuum):** Circuit optimization compiler; backend-agnostic; strong transpilation for trapped-ion

### Noise Mitigation Techniques
- **Zero-noise extrapolation (ZNE):** Run circuits at amplified noise levels; extrapolate to zero noise
- **Probabilistic error cancellation (PEC):** Decompose ideal gate as linear combination of noisy gates
- **Dynamical decoupling (DD):** Pulse sequences that refocus dephasing during idle periods
- **Symmetry verification:** Post-select on results consistent with known symmetries of the problem
- **M3 (Matrix-free Measurement Mitigation):** Scalable readout error mitigation; built into Qiskit Runtime

### Error Correction Codes (Active Research)
- **Surface codes:** ~1% threshold; leading candidate; requires 2D qubit grid with nearest-neighbor connectivity
- **Color codes:** Higher threshold but lower encoding rate; suitable for transversal gates
- **Bacon-Shor codes:** Subsystem codes; simplified syndrome measurement
- **GKP codes (Gottesman-Kitaev-Preskill):** Continuous-variable error correction; native to photonic platforms

### Transpilation & Optimization
- **Qiskit transpiler:** Converts logical circuit to native gate set and topology; optimization levels 0-3
- **TKET:** Route, optimize, and translate circuits; strong for deep circuits on NISQ hardware
- **BQSKit:** Berkeley QSKit; synthesis-based optimization; finds shortest equivalent circuit

---

## 4. Authoritative Data Sources

| Source | URL | Type | Update Frequency |
|--------|-----|------|-----------------|
| ArXiv quant-ph | https://arxiv.org/list/quant-ph/recent | Preprints | Daily |
| ArXiv quant-ph (month) | https://arxiv.org/list/quant-ph/month | Monthly digest | Monthly |
| IBM Quantum Learning | https://learning.quantum.ibm.com | Official curriculum | Ongoing |
| IBM Quantum Blog | https://www.ibm.com/quantum/blog | News & milestones | Weekly |
| Google Quantum AI Blog | https://quantumai.google/blog | Lab announcements | Monthly |
| Nature Quantum Information | https://www.nature.com/npjqi/ | Peer-reviewed | Weekly |
| Physical Review Letters | https://journals.aps.org/prl/ | Peer-reviewed | Weekly |
| Quantum Science and Technology | https://iopscience.iop.org/journal/2058-9565 | Peer-reviewed | Bimonthly |
| IonQ News | https://ionq.com/news | Hardware milestones | Monthly |
| Quantinuum News | https://www.quantinuum.com/news | Hardware milestones | Monthly |
| Rigetti Blog | https://www.rigetti.com/blog | Hardware milestones | Monthly |
| Preskill Lecture Notes (Ph229) | http://theory.caltech.edu/~preskill/ph229/ | Course notes | Updated periodically |
| Qiskit Documentation | https://docs.quantum.ibm.com | API reference | With releases |
| Qiskit Textbook | https://qiskit.org/learn | Open textbook | Community-driven |

---

## 5. Analytical Frameworks

### 5.1 Quantum Volume (QV) — IBM
- **Definition:** Largest random quantum circuit (of equal width and depth) that a device can successfully execute at ≥ 2/3 probability
- **Formula:** QV = max_n min(n, d(n))² where d(n) is achievable circuit depth for n qubits
- **Current leaders (as of early 2026):** IBM Heron r2 (QV 256+), Quantinuum H2 (QV 65536+ via trapped ion)
- **Use:** Compare devices across generations and vendors
- **Source:** Cross et al. (2019), arXiv:1811.12926

### 5.2 Algorithmic Qubits (AQ) — IonQ
- **Definition:** Number of qubits capable of successfully running a specific benchmark application (e.g., quantum chemistry, ML)
- **Advantage:** Captures real-world performance better than raw qubit count
- **IonQ Forte AQ29:** 29 algorithmic qubits (2023)
- **Source:** IonQ technical reports; https://ionq.com/algorithmic-qubits

### 5.3 Cross-Entropy Benchmarking (XEB) — Google
- **Definition:** Fidelity metric comparing output distribution of quantum device to ideal simulation
- **Formula:** F_XEB = (⟨p_ideal⟩_samples - 1/2^n) / (ideal expectation - 1/2^n)
- **Used in:** Google's quantum supremacy claim (Sycamore, 2019); ongoing Willow benchmarks
- **Source:** Boixo et al. (2018), arXiv:1608.00263

### 5.4 Gate Fidelity Standards
- **Single-qubit gate fidelity:** Target > 99.9% for FTQC; current NISQ best: 99.95%+ (trapped ion), 99.9% (superconducting)
- **Two-qubit gate fidelity:** Target > 99% for FTQC; current best: 99.9% (trapped ion H2), 99.5% (IBM Heron)
- **Readout fidelity:** Target > 99.9%; current best: 99.8% (trapped ion)
- **T1 (energy relaxation):** Typical superconducting: 200-500 µs; trapped ion: seconds to minutes
- **T2 (dephasing):** Typical superconducting: 100-300 µs; trapped ion: seconds

### 5.5 Nielsen & Chuang Curriculum Framework
The skill maps all concept modules to the following chapters:
- Ch. 1-2: Qubits, quantum gates, quantum circuits (Beginner modules 1-3)
- Ch. 3: Quantum Fourier Transform and phase estimation (Advanced module 6)
- Ch. 5-6: Quantum algorithms — search, factoring (Intermediate-Advanced modules 5-6)
- Ch. 7: Quantum computers — physical realizations (all hardware tracks)
- Ch. 10: Quantum error correction (Advanced module 7)

### 5.6 NISQ-vs-FTQC Classification Framework
For every circuit design request, sub-circuit-designer classifies the output:
- **NISQ-feasible:** ≤ 50 qubits, circuit depth ≤ T2/gate_time × fidelity_budget, no error correction required
- **NISQ-challenging:** 50-500 qubits or deep circuits; requires noise mitigation (ZNE, PEC, DD)
- **FTQC-required:** RSA-scale Shor's, large-scale quantum chemistry, any logical qubit computation

---

## 6. Self-Update Protocol

### Crawl Configuration

```python
CRAWL_SOURCES = [
    {
        "name": "arxiv_quant_ph",
        "url": "https://arxiv.org/list/quant-ph/recent",
        "type": "arxiv",
        "parser": "arxiv_rss",
        "max_items": 50,
        "relevance_keywords": [
            "quantum circuit", "quantum computing", "qubit", "quantum gate",
            "quantum error correction", "surface code", "NISQ", "quantum algorithm",
            "superconducting qubit", "trapped ion", "quantum hardware", "Qiskit",
            "quantum volume", "quantum advantage", "quantum supremacy",
            "fault tolerant quantum", "logical qubit", "quantum benchmark"
        ]
    },
    {
        "name": "ibm_quantum_blog",
        "url": "https://www.ibm.com/quantum/blog",
        "type": "blog",
        "parser": "html_article_list",
        "max_items": 10
    },
    {
        "name": "google_quantum_ai",
        "url": "https://quantumai.google/blog",
        "type": "blog",
        "parser": "html_article_list",
        "max_items": 10
    },
    {
        "name": "nature_quantum_info",
        "url": "https://www.nature.com/npjqi/",
        "type": "journal",
        "parser": "nature_toc",
        "max_items": 20
    },
    {
        "name": "physical_review_letters",
        "url": "https://journals.aps.org/prl/issues",
        "type": "journal",
        "parser": "aps_toc",
        "max_items": 15,
        "filter": "quantum"
    },
    {
        "name": "ionq_news",
        "url": "https://ionq.com/news",
        "type": "blog",
        "parser": "html_article_list",
        "max_items": 5
    },
    {
        "name": "quantinuum_news",
        "url": "https://www.quantinuum.com/news",
        "type": "blog",
        "parser": "html_article_list",
        "max_items": 5
    },
    {
        "name": "arxiv_quant_ph_month",
        "url": "https://arxiv.org/list/quant-ph/month",
        "type": "arxiv",
        "parser": "arxiv_rss",
        "max_items": 30,
        "relevance_keywords": ["quantum circuit", "quantum hardware", "quantum error correction"]
    }
]

RELEVANCE_THRESHOLD = 0.60
MIN_KEYWORD_MATCHES = 2
SCHEDULE = "weekly (Sunday 02:00 UTC)"
KNOWLEDGE_BRAIN_PATH = "D:/Dungchan/skill_adv/245/SECOND-KNOWLEDGE-BRAIN.md"
```

### Append Format

Every new entry appended to the Research Papers table or Update Log must follow this format:

```markdown
### [YYYY-MM-DD] {Title}
- **Authors:** {Last, F. et al.}
- **Venue:** {journal/conference/blog name}
- **DOI/URL:** {https://...}
- **Relevance Score:** {0.0-1.0}
- **Relevance:** {1-2 sentences: why this is relevant to quantum circuit design education}
- **Key Finding:** {1-2 sentences: what was discovered, demonstrated, or announced}
```

---

## 7. Knowledge Update Log

### [2026-06-19] Initial Knowledge Base Population
- **Source:** Manual curation by skill architect
- **New entries:** 19 research papers, 5 analytical frameworks, 8 core concepts, 14 data sources, 5 tools
- **Scope:** Foundational papers (1982-2024), all major hardware platforms, leading curricula
- **Next crawl scheduled:** 2026-06-26 (Sunday 02:00 UTC)

---

*End of SECOND-KNOWLEDGE-BRAIN.md. Use `tools/knowledge_updater.py` to add new entries.*
