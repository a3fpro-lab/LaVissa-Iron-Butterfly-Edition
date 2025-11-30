"""
Cosmology TRP Glue
==================

Hooks for Hartle–Hawking Vireon TRP (HHV-TRP-Engine):

- Geometric exit entropy: S_geom = 3π / (G H_I²)
- TRP decomposition: R = log(S_geom / S_0), P = exp(-μ C(ε))
- Anisotropy bound: T = R × P ≥ T_min ⇒ |ε| ≤ |ε|_max(N_e, H_I)

This module is a thin wrapper; the heavy lifting lives in the
HHV-TRP-Engine repository. Here we provide simple functions that
encode the key formulas and can be called from experiments.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from lavissa_core import TRPConfig, compute_T


@dataclass
class CosmologyTRPConfig:
    """
    Configuration for cosmological TRP calculations.
    """
    G: float = 1.0      # Newton's constant in chosen units
    H_I: float = 1.0    # Inflationary Hubble scale
    S_0: float = 1.0    # Reference entropy scale
    mu: float = 1.0     # Anisotropy cost coefficient
    t_min: float = 0.0  # T_min


def geometric_exit_entropy(cfg: CosmologyTRPConfig) -> float:
    """
    Compute S_geom = 3π / (G H_I²).
    """
    return 3.0 * math.pi / (cfg.G * cfg.H_I * cfg.H_I)


def R_from_entropy(cfg: CosmologyTRPConfig) -> float:
    """
    Compute R = log(S_geom / S_0).
    """
    S_geom = geometric_exit_entropy(cfg)
    return math.log(S_geom / cfg.S_0)


def P_from_anisotropy(cfg: CosmologyTRPConfig, epsilon: float, C_eps) -> float:
    """
    Compute P = exp(-μ C(ε)).

    C_eps : callable
        Cost functional C(ε) provided by the caller.
    """
    cost = C_eps(epsilon)
    return math.exp(-cfg.mu * cost)


def TRP_from_cosmology(
    cfg: CosmologyTRPConfig,
    epsilon: float,
    C_eps,
) -> float:
    """
    Compute T = R × P for given anisotropy ε and cost C(ε).
    """
    R_val = R_from_entropy(cfg)
    P_val = P_from_anisotropy(cfg, epsilon, C_eps)
    trp_cfg = TRPConfig(t_min=cfg.t_min, lambda_u=1.0)
    return compute_T(R_val, P_val, trp_cfg)
