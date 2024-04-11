#!/usr/bin/env python3
import argparse

from pprint import pprint
from dataclasses import dataclass
from argparse import ArgumentDefaultsHelpFormatter


@dataclass
class RewardRiskData:
    shares: int
    entry: str
    target: str
    stop: str
    gain: str
    loss: str
    position_size: str
    ratio: float


class RewardRiskCalculator:
    def __init__(self, *, rr: int) -> None:
        self._rr = rr

    def calculate_reward_risk_ratio(
            self,
            *,
            gain_target: float,
            entry: float,
            target: float
    ) -> RewardRiskData:
        size_unit = 1
        while True:
            try:
                shares = size_unit / entry
                gain = (target - entry) * shares
                adjustment_factor = gain_target / gain
                break
            except ZeroDivisionError:
                size_unit *= 10
                print(
                    f"trying again on adjustment factor "
                    f"with size_unit={size_unit}")
                pass

        shares = int(size_unit / entry * adjustment_factor + 1)
        delta_unit = (target - entry) / self._rr
        stop = entry - delta_unit
        gain = (target - entry) * shares
        loss = (entry - stop) * shares

        return RewardRiskData(
            ratio=self._rr,
            shares=shares,
            entry=f"${entry:.2f}",
            stop=f"${stop:.2f}",
            target=f"${target:.2f}",
            gain=f"${gain:.2f}",
            loss=f"${loss:.2f}",
            position_size=f"${entry * shares:.2f}"
        )


def floatify(expr: str) -> float:
    return float(eval(expr))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reward to risk calculator. Displays information in the "
                    "order of how one would input information into Fidelity "
                    "Active Trader Pro OTOCO form",
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-r",
        "--rr",
        default=3,
        help="reward to risk ratio as an integer",
        type=int
    )
    parser.add_argument(
        "-g",
        "--gain-target",
        default=300,
        help="gain target",
        type=float
    )
    parser.add_argument(
        "ENTRY",
        help="purchase price. This accepts expressions",
        type=floatify
    )
    parser.add_argument(
        "TARGET",
        help="price target. This accepts expressions",
        type=floatify
    )
    args = parser.parse_args()

    rr = RewardRiskCalculator(rr=args.rr)
    pprint(
        rr.calculate_reward_risk_ratio(
            gain_target=args.gain_target,
            entry=args.ENTRY,
            target=args.TARGET
        )
    )


if __name__ == '__main__':
    main()
