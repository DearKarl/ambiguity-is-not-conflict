"""Emit the deterministic MV-1 ideal-yield sensitivity table.

This is protocol arithmetic only. It uses no repository, medical, model, or
record-level data. The calculation assumes perfect report-screen polarity,
either 128 or 150 independent candidates in each polarity, and one common
independent probability that a candidate yields an evaluable intact/MV-1
sibling block.
"""

from __future__ import annotations

import csv
import math
import sys


SCREENED_PER_POLARITY_OPTIONS = (128, 150)
REQUIRED_PER_POLARITY = 108
EVALUABLE_PROBABILITIES = (0.80, 0.825, 0.85, 0.875, 0.90, 0.925, 0.95)
JOINT_YIELD_TARGET = 0.90


def binomial_upper_tail(n: int, threshold: int, probability: float) -> float:
    """Return P[X >= threshold] for X ~ Binomial(n, probability)."""

    return sum(
        math.comb(n, k)
        * probability**k
        * (1.0 - probability) ** (n - k)
        for k in range(threshold, n + 1)
    )


def minimum_probability_for_joint_target(
    n: int,
    threshold: int,
    joint_target: float,
) -> float:
    """Solve the equal-yield probability needed in two independent strata."""

    lower, upper = 0.0, 1.0
    for _ in range(100):
        midpoint = (lower + upper) / 2.0
        joint_probability = binomial_upper_tail(n, threshold, midpoint) ** 2
        if joint_probability >= joint_target:
            upper = midpoint
        else:
            lower = midpoint
    return upper


def main() -> int:
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(
        (
            "screened_per_polarity",
            "required_evaluable_per_polarity",
            "independent_pair_evaluable_probability",
            "expected_evaluable_per_polarity",
            "probability_meet_one_polarity",
            "probability_meet_both_polarities",
            "minimum_equal_yield_for_90pct_joint_probability",
            "assumption_scope",
        )
    )
    for screened_per_polarity in SCREENED_PER_POLARITY_OPTIONS:
        minimum_yield = minimum_probability_for_joint_target(
            screened_per_polarity,
            REQUIRED_PER_POLARITY,
            JOINT_YIELD_TARGET,
        )
        for evaluable_probability in EVALUABLE_PROBABILITIES:
            one = binomial_upper_tail(
                screened_per_polarity,
                REQUIRED_PER_POLARITY,
                evaluable_probability,
            )
            writer.writerow(
                (
                    screened_per_polarity,
                    REQUIRED_PER_POLARITY,
                    f"{evaluable_probability:.3f}",
                    f"{screened_per_polarity * evaluable_probability:.3f}",
                    f"{one:.6f}",
                    f"{one * one:.6f}",
                    f"{minimum_yield:.9f}",
                    "perfect_screen_polarity_and_independent_equal_yield",
                )
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
