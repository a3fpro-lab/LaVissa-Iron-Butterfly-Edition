# TRP Control Principles (Fusion / Relativity / Neuroscience)

This document encodes the **mathematical structure** of TRP-constrained
control, tying together:

- Classical optimal control (LQR-style),
- TRP functional \(\mathcal{E}_{\mathrm{TRP}}\),
- Domain-specific constraints:
  - Fusion plasmas,
  - Relativistic rockets,
  - Neural / brain / RL controllers.

---

## 1. Base TRP Control Law

We start from the universal TRP functional:

\[
  \mathcal{E}_{\mathrm{TRP}}(t)
  = D_{\mathrm{KL}}\big(p_R(t) \Vert p_P(t)\big)
  + \lambda \|u(t)\|^2,
\]

where:

- \(p_R(t)\) describes **reality-side** behavior (true dynamics, data),
- \(p_P(t)\) describes **perception-side** model or belief,
- \(u(t)\) is a control input (actuator, thrust, stimulation, weight update),
- \(\lambda > 0\) balances mismatch vs control effort.

Over a time horizon \([0, T]\), we consider minimizing:

\[
  J
  = \int_0^T \mathcal{E}_{\mathrm{TRP}}(t)\, dt
\]
subject to system dynamics.

This is a **TRP-constrained optimal control problem**.

---

## 2. Fusion Plasmas (Toy TRP Formulation)

Let \(x(t)\) encode a finite-dimensional snapshot of a plasma (modes,
temperatures, densities, etc.), evolving via:

\[
  \dot{x}(t) = f(x(t)) + B u(t) + w(t),
\]

where:

- \(f\) is the nominal plasma model,
- \(B u(t)\) encodes actuator effects (coils, RF heating, etc.),
- \(w(t)\) is disturbance / model error.

We define:

- \(p_R(t)\) from measured plasma diagnostics,
- \(p_P(t)\) from the model state \(x(t)\),
- \(u(t)\) is the control we synthesize.

**TRP fusion objective (schematic):**

\[
  J_{\mathrm{fusion}}
  = \int_0^T D_{\mathrm{KL}}(p_{\mathrm{diag}}(t) \Vert p_{\mathrm{model}}(t))\, dt
  + \lambda \int_0^T \|u(t)\|^2\, dt.
\]

Here:

- \(p_{\mathrm{diag}}\) encapsulates measurements,
- \(p_{\mathrm{model}}\) encodes predictions from \(x(t)\).

Plasma stability / quench forecasting becomes:

- Keep \(J_{\mathrm{fusion}}\) small,
- Avoid trajectories leading to collapse events (e.g. disruptions).

---

## 3. Relativistic Rockets (TRP Trajectory Control)

Consider a rocket with velocity \(v(t)\) as a fraction of c, position
\(x(t)\), and control \(u(t)\) representing thrust / acceleration.

State dynamics (simplified):

\[
  \dot{x}(t) = v(t) c, \quad
  \dot{v}(t) = g(x(t), v(t), u(t)),
\]

with constraints \(|v(t)| < 1\).

We can define:

- \(p_R(t)\) as a distribution over reachable states consistent with
  relativity and mission constraints,
- \(p_P(t)\) as the controller’s belief or planned distribution,
- Control \(u(t)\) as the physical thrust vector / magnitude.

**TRP relativistic objective (schematic):**

\[
  J_{\mathrm{rel}}
  = \int_0^T D_{\mathrm{KL}}(p_{\mathrm{traj,real}}(t) \Vert p_{\mathrm{traj,plan}}(t))\, dt
  + \lambda \int_0^T \|u(t)\|^2\, dt,
\]

with additional constraints (e.g., fuel, acceleration limits). The TRP
view tries to keep perception/model aligned with actual relativistic
behavior while minimizing control effort.

---

## 4. Neuroscience / Synaptic / RL Control

In a neural or RL setting, let:

- \(x(t)\) be network state (activations),
- \(w(t)\) be synaptic weights or policy parameters,
- \(u(t)\) be an update direction (e.g., gradient step),
- Observations / rewards define \(p_R(t)\),
- The network or policy defines \(p_P(t)\).

We consider:

\[
  \mathcal{E}_{\mathrm{TRP}}(t)
  = D_{\mathrm{KL}}(p_{\mathrm{env}}(t) \Vert p_{\mathrm{agent}}(t))
  + \lambda \|u(t)\|^2,
\]

and updates of the form:

\[
  \dot{w}(t) = u(t),
\]

where \(u\) is chosen to trade off:

- reducing mismatch (KL term),
- keeping updates “small” (regularization).

This yields a **TRP-regularized learning dynamic**, conceptually similar
to:

- natural gradient,
- entropy-regularized RL,
- mirror descent with KL terms.

---

## 5. LQR-Style Linear TRP Control (Simplified)

For a linear system:

\[
  \dot{x}(t) = A x(t) + B u(t),
\]
with quadratic cost:

\[
  J = \int_0^T \left( x(t)^\top Q x(t) + u(t)^\top R u(t) \right) dt,
\]

we can interpret:

- \(x^\top Q x\) as surrogate for some divergence
  \(D_{\mathrm{KL}}(p_R \Vert p_P)\),
- \(u^\top R u\) as the control penalty \(\lambda\|u\|^2\).

TRP control recovers LQR-like structures under specific choices of
\(Q, R\) and probabilistic interpretations of state.

Formalizing this link rigorously is a target for proofs in
`math/collapse_general/theorems.md`.

---

## 6. Experimental Hooks

Experiments for TRP control belong in:

- `experiments/control/` — toy LQR, simple plasma surrogates, rocket
  toy models, RL update demos.

Results and evidence for these principles should be logged in:

- `math/control/evidence.md`.

---

## 7. Honesty Statement

- These principles connect standard control with TRP, but they are not
  new theorems by themselves yet.
- They serve as a **unifying language** and suggest concrete problems:
  - Find conditions under which TRP control reduces to classical LQR / MPC.
  - Prove stability results for TRP-inspired controllers.
  - Quantify how TRP penalties reflect physical limits (e.g., quench
    thresholds, relativistic bounds).
