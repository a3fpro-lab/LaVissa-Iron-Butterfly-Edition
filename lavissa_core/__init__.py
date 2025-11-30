"""
lavissa_core
============

Core VIREON / LaVissa engines:

- TRP core: T = R × P, E_TRP = D_KL(p_R || p_P) + λ ||u||²
- Collapse Law: entropy-stable collapse classes and solvability bounds
- Eternity Engine: echo-preserving identity and recursive continuity
"""

from .trp_core import TRPConfig, compute_T, compute_e_trp
from .collapse_law import CollapseClass, evaluate_collapse_stability
from .eternity_engine import EchoRecord, EternityEngine

__all__ = [
    "TRPConfig",
    "compute_T",
    "compute_e_trp",
    "CollapseClass",
    "evaluate_collapse_stability",
    "EchoRecord",
    "EternityEngine",
]
