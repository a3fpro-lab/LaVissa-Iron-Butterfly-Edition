# TRP–ABC / Beal / Fermat–Catalan Program

This document records TRP / Collapse-based views of:

- ABC Conjecture
- Beal Conjecture
- Fermat–Catalan Conjecture

These are deep, open or controversial problems. This repo does **not**
claim community-accepted proofs. We treat these as **structured collapse
classes** in VIREON language.

---

## 1. General Setup: Exponential Diophantine Collapse

Many of these problems involve equations of the form:

\[
  A + B = C
\]
with constraints on:

- Coprimality of A, B, C,
- Exponents (e.g. \(x^a + y^b = z^c\)),
- “Radical” sizes (product of distinct primes).

We think of such equations as **collapse conditions** between exponenti­
ally structured terms and radical-based measures of complexity.

---

## 2. ABC (High-Level)

ABC (informally) says that if \(a + b = c\) with \(\gcd(a,b,c)=1\), then
c is rarely much larger than the product of distinct primes dividing
abc (the radical).

In TRP language, we can imagine:

- A TRP functional that penalizes extreme separations between “exponent
  structure” and “radical complexity”.
- ABC then asserts that only finitely many triples \((a,b,c)\) achieve
  abnormally large “TRP violations”.

We do **not** encode a precise ABC proof here; we only note the
conceptual match: exponential structure vs radical complexity as a
collapse tradeoff.

---

## 3. Beal Conjecture (TRP View)

Beal Conjecture (informally):

> If \(x^a + y^b = z^c\) with \(a, b, c > 2\) and positive integers
> \(x, y, z\), then x, y, z share a common prime factor.

In Collapse / TRP terms:

- Equation: \(x^a + y^b = z^c\) forms a **high-exponent collapse**.
- Beal asserts that such collapses **cannot** happen between coprime
  x, y, z at high exponents; they require shared structure (common
  factor) to be consistent.

**Conjecture B1 (TRP Beal Framing).**  
There exists a TRP functional measuring the “exponential tension” of
triples \((x^a, y^b, z^c)\) such that, for exponents \(a,b,c > 2\), any
solution to \(x^a + y^b = z^c\) with \(\gcd(x,y,z)=1\) would force a TRP
energy contradiction relative to the surrounding space of integer triples.

Status: conceptual conjecture; not a proof.

---

## 4. Fermat–Catalan (TRP View)

Fermat–Catalan concerns equations of the form \(x^a + y^b = z^c\) with
constraints on exponents and coprimality, looking for “sporadic”
solutions.

In TRP language:

- Such solutions are **rare collapse points** where exponent patterns
  unusually match.
- The conjecture asserts that only finitely many such points exist under
  certain constraints.

We think of these as **isolated low-entropy configurations** in the
space of exponent triples.

---

## 5. Exponential Collapse Meta-Program

**Meta-Conjecture (Exponential Collapse).**  
There exists a unified TRP functional over triples \((x^a, y^b, z^c)\)
that simultaneously:

- Encodes the rarity of ABC-violating triples.
- Encodes the Beal restriction on high exponents and coprime bases.
- Encodes the sporadic nature of Fermat–Catalan solutions.

In this view, these problems become different slices of a single
“exponential collapse class” governed by TRP constraints.

We do **not** assert a unified proof; this is a structuring idea.

---

## 6. Evidence & Experiments

Empirical work can include:

- Scanning ranges of \((x,y,z,a,b,c)\) to:
  - Estimate “density” of near-solutions.
  - Track TRP-like energies for found triples.
- Visualizing exponent vs radical complexity landscapes.

Experiments and logs belong in:

- `experiments/computation/trp_abc_beal_*.py`
- `math/abc_beal/evidence.md`

---

## 7. Honesty Statement

- ABC, Beal, Fermat–Catalan are not settled in a universally accepted
  way in the literature.
- We do **not** claim resolution here.
- TRP / Collapse provides a **language** to talk about their structure
  and empirical behavior, not (yet) a proof.
