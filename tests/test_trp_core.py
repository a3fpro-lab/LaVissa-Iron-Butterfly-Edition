"""
Basic tests for TRP core.

These are intentionally simple and can be run with:

    pytest tests/test_trp_core.py

or any test runner that understands plain asserts.
"""

from lavissa_core import TRPConfig, compute_T, compute_e_trp


def test_compute_T_simple():
    cfg = TRPConfig(t_min=1.0, lambda_u=1.0)
    T = compute_T(2.0, 0.75, cfg)
    assert T == 1.5
    assert T >= cfg.t_min


def test_e_trp_symmetry_and_control():
    cfg = TRPConfig(t_min=0.0, lambda_u=0.5)
    p_R = [0.5, 0.5]
    p_P = [0.5, 0.5]
    u = [1.0, 2.0]

    e_val = compute_e_trp(p_R, p_P, u, cfg)
    # KL = 0 for identical distributions
    # ||u||² = 1² + 2² = 5, λ = 0.5 => λ||u||² = 2.5
    assert abs(e_val - 2.5) < 1e-9
