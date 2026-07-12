"""Portfolio constraint helpers for minimum-risk optimization inputs."""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class PortfolioConstraints:
    """Explicit constraints for the first minimum-risk portfolio run."""

    long_only: bool = True
    min_weight: float = 0.0
    max_weight: float = 0.2
    min_quote_coverage: float = 0.95

    def __post_init__(self) -> None:
        if self.min_weight < 0:
            raise ValueError("min_weight cannot be negative")
        if self.max_weight <= 0:
            raise ValueError("max_weight must be positive")
        if self.min_weight > self.max_weight:
            raise ValueError("min_weight cannot exceed max_weight")
        if not 0 < self.min_quote_coverage <= 1:
            raise ValueError("min_quote_coverage must be in (0, 1]")


def validate_weights(weights: dict[str, float], constraints: PortfolioConstraints) -> None:
    if not weights:
        raise ValueError("weights are required")
    total = sum(weights.values())
    if not isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-9):
        raise ValueError("weights must sum to 1")
    for isin, weight in weights.items():
        if constraints.long_only and weight < 0:
            raise ValueError(f"negative weight for {isin}")
        if weight < constraints.min_weight:
            raise ValueError(f"weight below minimum for {isin}")
        if weight > constraints.max_weight:
            raise ValueError(f"weight above maximum for {isin}")


def equal_weight_seed(isins: list[str], constraints: PortfolioConstraints) -> dict[str, float]:
    if not isins:
        raise ValueError("at least one ISIN is required")
    weight = 1.0 / len(isins)
    weights = {isin: weight for isin in sorted(isins)}
    validate_weights(weights, constraints)
    return weights


def minimum_variance_two_asset_weight(
    *,
    left_variance: float,
    right_variance: float,
    covariance: float,
    constraints: PortfolioConstraints,
) -> dict[str, float]:
    denominator = left_variance + right_variance - (2 * covariance)
    raw_left = 0.5 if denominator == 0 else (right_variance - covariance) / denominator
    left = min(constraints.max_weight, max(constraints.min_weight, raw_left))
    right = 1.0 - left
    weights = {"left": left, "right": right}
    validate_weights(weights, constraints)
    return weights
