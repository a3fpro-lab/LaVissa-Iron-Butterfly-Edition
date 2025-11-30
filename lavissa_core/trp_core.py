"""
TRP Core
========

Implements the core TRP quantities:

- T = R × P, with T >= T_min
- E_TRP = D_KL(p_R || p_P) + λ ||u||²

This is intentionally light on dependencies so it can be imported in any
environment and upgraded later with NumPy / JAX / PyTorch.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Optional
import math


@dataclass
class TRPConfig:
    """
    Configuration for TRP computations.

    Attributes
    ----------
    t_min : float
        Minimum viable TRP (T_min).
    lambda_u : float
        Regularization weight λ on control effort ||u||².
    """

    t_min: float = 0.0
    lambda_u: float = 1.0


def compute_T(R: float, P: float, cfg: Optional[TRPConfig] = None) -> float:
    """
    Compute T = R × P and optionally enforce T >= T_min.

    Parameters
    ----------
    R : float
        Reality bandwidth.
    P : float
        Perception / processing gain.
    cfg : TRPConfig, optional
        Configuration including T_min. If provided, this function
        will not modify T, but you can check against cfg.t_min externally.

    Returns
    -------
    float
        The TRP scalar T.
    """
    T = R * P
    # No clamping here; caller can compare to cfg.t_min.
    return T


def _safe_log(x: float, eps: float = 1e-12) -> float:
    """Numerically safe log."""
    return math.log(max(x, eps))


def d_kl(p_R: Sequence[float], p_P: Sequence[float]) -> float:
    """
    Compute discrete Kullback–Leibler divergence D_KL(p_R || p_P).

    Parameters
    ----------
    p_R : sequence of float
        Reality-side probabilities.
    p_P : sequence of float
        Perception-side probabilities.

    Returns
    -------
    float
        KL divergence in nats.

    Notes
    -----
    - Both distributions are internally renormalized to sum to 1.
    - Entries <= 0 are treated as eps.
    """
    if len(p_R) != len(p_P):
        raise ValueError("p_R and p_P must have the same length")

    eps = 1e-12
    sum_R = sum(max(x, 0.0) for x in p_R)
    sum_P = sum(max(x, 0.0) for x in p_P)

    if sum_R <= 0 or sum_P <= 0:
        raise ValueError("Distributions must have positive total mass")

    kl = 0.0
    for r_raw, p_raw in zip(p_R, p_P):
        r = max(r_raw, eps) / sum_R
        p = max(p_raw, eps) / sum_P
        kl += r * (_safe_log(r) - _safe_log(p))

    return kl


def control_norm_sq(u: Sequence[float]) -> float:
    """
    Compute ||u||² (squared Euclidean norm) of a control vector u.

    Parameters
    ----------
    u : sequence of float
        Control vector.

    Returns
    -------
    float
        Squared norm.
    """
    return sum(float(x) * float(x) for x in u)


def compute_e_trp(
    p_R: Sequence[float],
    p_P: Sequence[float],
    u: Sequence[float],
    cfg: Optional[TRPConfig] = None,
) -> float:
    """
    Compute E_TRP = D_KL(p_R || p_P) + λ ||u||².

    Parameters
    ----------
    p_R : sequence of float
        Reality-side probabilities.
    p_P : sequence of float
        Perception-side probabilities.
    u : sequence of float
        Control vector.
    cfg : TRPConfig, optional
        Configuration with lambda_u (λ). If None, λ = 1.0 is used.

    Returns
    -------
    float
        E_TRP value.
    """
    if cfg is None:
        cfg = TRPConfig()

    kl = d_kl(p_R, p_P)
    norm_sq = control_norm_sq(u)
    return kl + cfg.lambda_u * norm_sq
