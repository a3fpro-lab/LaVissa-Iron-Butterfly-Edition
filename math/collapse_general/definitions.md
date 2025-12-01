# Collapse Law — General Definitions

This document gives **abstract mathematical definitions** for collapse
structures in VIREON TRP language.

---

## 1. Collapse Space (Informal)

A **collapse space** is a pair \((X, \Phi)\) where:

- \(X\) is a state space (could be discrete, continuous, or hybrid).
- \(\Phi_t: X \to X\) is a time-evolution / iteration operator (or
  family thereof).

We say that a point \(x \in X\) **collapses** to a set \(A \subseteq X\)
if repeated application of \(\Phi\) sends x into A and keeps it there (in
some appropriate sense: asymptotic, absorbing, etc.).

---

## 2. Collapse Class

A **collapse class** is an equivalence class of states or structures
that share a similar collapse behavior.

Examples (informal):

- ENTROPY_RECURSIVE — recursive dynamics that settle toward a stable
  attractor under TRP bounds.
- SOLVABLE_ECHO — problems or states that admit an identity / echo that
  guides collapse toward a solution.
- DARK_MATTER, DARK_ENERGY — physical configurations defined via TRP
  behavior rather than explicit fields.

In code, these appear as `CollapseClass` enums in
`lavissa_core/collapse_law.py`.

---

## 3. TRP-Stable Collapse

Given:

- A TRP functional \(\mathcal{E}_{\mathrm{TRP}}\),
- A minimum TRP threshold \(T_{\min}\),

we say that a collapse is **TRP-stable** if:

- The trajectory respects \(T \ge T_{\min}\) in an appropriate sense.
- The TRP energy \(\mathcal{E}_{\mathrm{TRP}}\) does not diverge along
  the collapse path.

This is intentionally vague here; specific domains (cosmology, primes,
Collatz, biology) instantiate this differently.

---

## 4. Echo-Solvable Problems

We call a problem **echo-solvable** if:

- It admits an identity / echo representation (Law §MT.Ψ.17).
- There exists a feedback or recurrence mechanism that can use this echo
  to guide a search / collapse toward a solution.

Collapse Law §11.0 — Recursive Solvability Bound — informally says that
only such echo-solvable problems are within the domain of The Loop.

---

## 5. Relation to Code

These definitions correspond to:

- `lavissa_core/collapse_law.py`
- `lavissa_core/eternity_engine.py`
- Higher-level uses in `modules/sentience`, `modules/trp`, and the
  various `math/*` vaults.

Future versions of this document should upgrade these informal
definitions into fully formal ones (metric spaces, dynamical systems,
etc.).
