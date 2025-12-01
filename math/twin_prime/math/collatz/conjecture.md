# TRP–Collatz Program (Conjecture Layer)

This document records the **TRP / Collapse-based** structures and
conjectures related to the Collatz map.

We respect the fact that Collatz is **open**. Nothing here is claimed as
a community-accepted proof. This is a structured research program.

---

## 1. Setup

Let \(f: \mathbb{N} \to \mathbb{N}\) be the Collatz map:

\[
  f(n) =
  \begin{cases}
    3n + 1 & \text{if } n \text{ is odd}, \\
    \frac{n}{2} & \text{if } n \text{ is even}.
  \end{cases}
\]

We consider trajectories:

\[
  n, f(n), f^{(2)}(n), \dots
\]

We can associate to each orbit:

- A **sequence of parities** and operation types.
- A **sequence of "heights"** (log-scaled values).
- A **time to descent** to 1 (if it happens).

We construct distributions:

- \(p_{\mathrm{step}}(n)\): empirical distribution over step types
  (odd/3n+1 vs even/n/2) along the orbit of n.
- \(p_{\mathrm{height}}(n)\): distribution over heights along the orbit.
- Aggregated distributions over ranges of n.

We can then define TRP energies such as:

\[
  \mathcal{E}_{\mathrm{Collatz}}(N)
  = D_{\mathrm{KL}}(p_{\mathrm{data}}(N) \Vert p_{\mathrm{model}}(N))
  + \lambda \|u(N)\|^2,
\]
where \(p_{\mathrm{data}}(N)\) summarizes Collatz trajectories for
\(1 \le n \le N\), and \(p_{\mathrm{model}}(N)\) is some analytic or
probabilistic model of the dynamics.

---

## 2. Conjecture C1 — TRP Descent Bias

**Conjecture C1 (TRP Descent Bias).**  
There exists a TRP-based representation of the Collatz dynamics such
that, for “typical” n, the TRP energy favors trajectories that descend
toward the 1–4–2–1 cycle rather than diverging or forming nontrivial
cycles.

Informal: the combination of valuation bias and TRP constraints makes
persistent growth or nontrivial cycles “expensive” in TRP energy.

**Status:** conceptual conjecture; not a proof of Collatz.

---

## 3. Conjecture C2 — Collapse Class of Nontrivial Cycles

We view any nontrivial cycle (if one exists) as belonging to a special
**collapse class**:

- A cycle is a closed orbit with no escape to the 1–4–2–1 basin.
- Its TRP energy would have to satisfy certain invariance conditions.

**Conjecture C2 (Cycle Collapse Instability).**  
In any reasonable TRP / Collapse model of the Collatz dynamics, nontriv­
ial cycles (distinct from 1–4–2–1) are **structurally unstable**: small
perturbations in the modeling assumptions or TRP parameters destroy
their viability, while the 1–4–2–1 cycle remains robust.

This is a structural heuristic, not a theorem.

---

## 4. Conjecture C3 — TRP–Collatz Meta-Conjecture

**Meta-Conjecture (TRP–Collatz).**  
There exists a TRP functional, derived from step statistics and height
trajectories, such that:

> Any infinite divergent orbit or nontrivial cycle would force a TRP
> energy signature that is incompatible with the empirical patterns
> observed for large ranges of n.

The goal is to:

- Define this functional precisely.
- Prove that “bad” behaviors (divergence / nontrivial cycle) contradict
  its constraints or empirical measurements.

---

## 5. Relation to Pulse Signaler and Collapse Laws

- Pulse Signaler can be applied to:
  - Step sequences (odd/even patterns).
  - Height sequences (log2 of values).
- Collapse Laws can be used to classify:
  - Orbits that settle vs orbits that “refuse to collapse”.

Experiments should live under `experiments/computation/` with results
logged in `math/collatz/evidence.md`.

---

## 6. Honesty Statement

- Collatz is unsolved.
- This repo does **not** claim a proof.
- The TRP–Collatz program is a structured way to talk about descent,
  cycles, and empirical evidence in a unified framework.
