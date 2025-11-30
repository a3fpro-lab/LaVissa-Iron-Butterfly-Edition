"""
TRP Module
==========

High-level interface for TRP-based systems:

- TRP Time (T = R × P with KL-Leash)
- Hartle–Hawking Vireon TRP (HHV-TRP-Engine)
- Links to cosmology, control, and complexity experiments.

This package is intentionally thin: it imports core math from `lavissa_core`
and provides glue functions / configs that wrap the specialized repos:

- Vireon_TRP_Time
- HHV-TRP-Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any

from lavissa_core import TRPConfig, compute_T, compute_e_trp


@dataclass
class TRPTimeState:
    """
    Minimal TRP Time state container.

    Attributes
    ----------
    reality_bandwidth : float
        R term.
    perception_gain : float
        P term.
    config : TRPConfig
        TRP configuration (T_min, λ for control).
    """
    reality_bandwidth: float
    perception_gain: float
    config: TRPConfig


def trp_time_step(
    state: TRPTimeState,
    p_R,
    p_P,
    u,
) -> Dict[str, Any]:
    """
    One TRP Time update step.

    Parameters
    ----------
    state : TRPTimeState
        Current TRP Time state (R, P, config).
    p_R, p_P : sequence of float
        Reality- and perception-side distributions.
    u : sequence of float
        Control vector (e.g., policy update, control action).

    Returns
    -------
    dict
        {
          "T": T,
          "E_TRP": E_TRP,
          "viable": bool
        }
    """
    T_val = compute_T(state.reality_bandwidth, state.perception_gain, state.config)
    e_val = compute_e_trp(p_R, p_P, u, state.config)
    viable = T_val >= state.config.t_min
    return {"T": T_val, "E_TRP": e_val, "viable": viable}
