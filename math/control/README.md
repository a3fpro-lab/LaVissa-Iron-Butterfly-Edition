# TRP Control Vault (Fusion / Relativity / Neuroscience)

This vault holds the **control-theoretic** side of LaVissa:

- TRP-constrained optimal control principles
- Applications to:
  - **Fusion plasmas** (stability, quench prediction)
  - **Relativistic rockets** (near-c trajectories under TRP)
  - **Neural / brain / RL control** (synaptic updates under TRP)

It links:

- The universal functional  
  \[
    \mathcal{E}_{\mathrm{TRP}} = D_{\mathrm{KL}}(p_R \Vert p_P) + \lambda\|u\|^2
  \]
- Classical control (LQR, MPC, feedback laws)
- Physical constraints (causality, relativistic bounds, plasma limits)

Documents here:

- `principles.md` — TRP control principles and formulations.
- `evidence.md` — logs of experiments and simulations.

Experiments live mostly under:

- `experiments/control/`
- Possibly `experiments/quantum/` (for relativistic or quantum control)
- With code in `modules/` (future TRP control modules).
