import argparse
import json
import sys
import logging

from dataclasses import dataclass
from argparse import ArgumentDefaultsHelpFormatter
from typing import Optional


def floatify(expr: str) -> float:
    return float(eval(expr))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Given risk/reward, desired total realized gain, "
                    "objective entry, and target, print the information bound "
                    "to those parameters that should be entered into a "
                    "Fidelity Active Trader Pro OTOCO form",
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action='store_true',
        help="verbose logging output"
    )
    parser.add_argument(
        "-r",
        "--reward-to-risk",
        default=3,
        help="reward to risk ratio as an integer",
        type=float
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

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    reward_risk: float = args.reward_to_risk
    total_gain: float = args.total_gain
    prev_loss: Optional[float] = args.prev_loss
    entry: float = args.ENTRY
    target: float = args.TARGET

    gain_single_share = target - entry
    unit = gain_single_share/reward_risk
    stop_price = entry - unit

    quantity = int(total_gain/gain_single_share)
    loss_single_share = entry - stop_price
    total_loss = loss_single_share*quantity

    if prev_loss is None:
        print(
            json.dumps(
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
                indent=4
            )
        )
    else:
        init_entry = entry
        init_total_gain = total_gain

        while True:
            adjusted_cost_basis_single_share = prev_loss/quantity
            entry = init_entry + adjusted_cost_basis_single_share

            gain_single_share = target - entry
            unit = gain_single_share/reward_risk
            stop_price = entry - unit

            loss_single_share = entry - stop_price
            total_loss = loss_single_share*quantity
            total_gain = gain_single_share*quantity

            logging.info(
                json.dumps(
                    {
                        "quantity": quantity,
                        "limit price buy": f"${init_entry:.2f}",
                        "limit price sell": f"${target:.2f}",
                        "stop price loss": f"${stop_price:.2f}",
                        "adjusted cost basis": f"${entry:.2f}",
                        "total realized gain": f"${total_gain:.2f}",
                        "total realized loss": f"${total_loss:.2f}",
                        "ratio": reward_risk,
                        "position_size": f"${entry * quantity:.2f}"
                    },
                    indent=4
                )
            )

            if entry > target:
                logging.error(f"entry {entry} is greater than target {target}")
                break
            elif stop_price > target:
                logging.error(
                    f"stop price {stop_price} is greater than target {target}")
                break
            elif total_gain >= init_total_gain:
                break

            quantity += 1


        print(
            json.dumps(
                {
                    "quantity": quantity,
                    "limit price buy": f"${init_entry:.2f}",
                    "limit price sell": f"${target:.2f}",
                    "stop price loss": f"${stop_price:.2f}",
                    "adjusted cost basis": f"${entry:.2f}",
                    "total realized gain": f"${total_gain:.2f}",
                    "total realized loss": f"${total_loss:.2f}",
                    "ratio": reward_risk,
                    "position_size": f"${entry * quantity:.2f}"
                },
                indent=4
            )
        )


if __name__ == '__main__':
    main()
