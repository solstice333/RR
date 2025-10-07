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
        "--total-gain",
        default=300,
        help="total realized gain",
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
        help="objective entry price",
        type=floatify
    )
    parser.add_argument(
        "TARGET",
        help="target price",
        type=floatify
    )
    args = parser.parse_args()

    reward_risk = args.rr
    total_gain: float = args.total_gain
    prev_loss: float = args.prev_loss
    entry: float = args.ENTRY
    target: float = args.TARGET

    gain_single_share = target - entry
    unit = gain_single_share/reward_risk
    stop_price = entry - unit

    quantity = total_gain/gain_single_share
    loss_single_share = entry - stop_price
    total_loss = loss_single_share*quantity

    json.dump(
        {
            "quantity": quantity,
            "limit price buy": f"${entry:.2f}",
            "limit price sell": f"${target:.2f}",
            "stop price loss": f"${stop_price:.2f}",
            "total realized gain": f"${total_gain:.2f}",
            "total realized loss": f"${total_loss:.2f}",
            "ratio": reward_risk,
            "position_size": f"${entry * quantity:.2f}"
        },
        sys.stdout,
        indent=4
    )


if __name__ == '__main__':
    main()
