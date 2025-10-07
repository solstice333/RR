import argparse
import json
import sys

from dataclasses import dataclass
from argparse import ArgumentDefaultsHelpFormatter


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
        "-l",
        "--prev-loss",
        default=0,
        help="previous loss to account for adjusted cost basis",
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

    size_unit = 1
    risk_reward = args.rr
    gain_target: float = args.gain_target
    entry: float = args.ENTRY
    target: float = args.TARGET
    prev_loss: float = args.prev_loss
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
    delta_unit = (target - entry) / risk_reward
    stop = entry - delta_unit
    gain = (target - entry) * shares
    loss = (entry - stop) * shares

    json.dump(
        {
            "quantity": shares,
            "limit price buy": f"${entry:.2f}",
            "limit price sell": f"${target:.2f}",
            "stop price loss": f"${stop:.2f}",
            "total realized gain": f"${gain:.2f}",
            "total realized loss": f"${loss:.2f}",
            "ratio": args.rr,
            "position_size": f"${entry * shares:.2f}"
        },
        sys.stdout,
        indent=4
    )


if __name__ == '__main__':
    main()
