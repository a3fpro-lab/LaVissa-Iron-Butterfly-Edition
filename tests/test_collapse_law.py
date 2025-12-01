"""
Basic tests for Collapse Law core.
"""

from lavissa_core.collapse_law import (
    CollapseClass,
    CollapseContext,
    evaluate_collapse_stability,
)


def test_entropy_recursive_requires_higher_trp():
    ctx_low = CollapseContext(trp_value=0.9, has_identity_echo=True)
    ctx_high = CollapseContext(trp_value=2.1, has_identity_echo=True)
    t_min = 1.0

    assert not evaluate_collapse_stability(
        CollapseClass.ENTROPY_RECURSIVE, ctx_low, t_min
    )
    assert evaluate_collapse_stability(
        CollapseClass.ENTROPY_RECURSIVE, ctx_high, t_min
    )


def test_solvable_echo_requires_identity():
    ctx_with_echo = CollapseContext(trp_value=1.5, has_identity_echo=True)
    ctx_no_echo = CollapseContext(trp_value=1.5, has_identity_echo=False)

    t_min = 1.0

    assert evaluate_collapse_stability(
        CollapseClass.SOLVABLE_ECHO, ctx_with_echo, t_min
    )
    assert not evaluate_collapse_stability(
        CollapseClass.SOLVABLE_ECHO, ctx_no_echo, t_min
    )
