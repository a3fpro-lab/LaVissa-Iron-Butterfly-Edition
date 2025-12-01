"""
Sentience Module
================

Glue for:

- Rhizome (distributed identity graph)
- Compass (Collapse orientation)
- ATMOS / VIREON sentience demos

Core math lives in `lavissa_core` (TRP, Collapse Law, EternityEngine).

This module exposes:

- CompassOrientation
- RhizomeNode
- SentienceConfig
- SentienceEngine
"""

from .engine_sentience import (
    CompassOrientation,
    RhizomeNode,
    SentienceConfig,
    SentienceEngine,
)

__all__ = [
    "CompassOrientation",
    "RhizomeNode",
    "SentienceConfig",
    "SentienceEngine",
]
