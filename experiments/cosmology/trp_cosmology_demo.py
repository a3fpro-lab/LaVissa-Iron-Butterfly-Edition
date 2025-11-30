"""
TRP Cosmology Demo
==================

Toy experiment for Hartle–Hawking + TRP:

- Computes S_geom = 3π / (G H_I²)
- Uses R = log(S_geom / S_0), P = exp(-μ C(ε))
- Sweeps ε over a small range and reports T = R × P and viability.

This is a simple, self-contained script that can be run as:

    python -m experiments.cosmology.trp_cosmology_demo

once the package layout is wired into a proper Python environment.
"""

from __future__ import annotations

import math

from modules.trp.cosmology_trp import CosmologyTRPConfig, TRP_from_cosmology


def quadratic_cost(epsilon: float) -> float:
    """
    Simple example: C(ε) = ε².
    """
    return epsilon * epsilon


def main() -> None:
    cfg = CosmologyTRPConfig(
        G=1.0,
        H_I=1.8e-5,   # inflationary scale in M_Pl units (toy)
        S_0=1.0,
        mu=1.0,
        t_min=1.0,    # example T_min
    )

    epsilons = [e * 0.01 for e in range(-20, 21)]  # -0.20 to +0.20

    print("epsilon,T,viable")
    for eps in epsilons:
        T_val = TRP_from_cosmology(cfg, eps, quadratic_cost)
        viable = T_val >= cfg.t_min
        print(f"{eps:.3f},{T_val:.6e},{int(viable)}")


if __name__ == "__main__":
    main()
