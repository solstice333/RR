# RR

## Description

Reward to risk calculator. Displays information in the order of how one would input information into Fidelity Active Trader Pro OTOCO form

## Usage

```
usage: rr.py [-h] [-v] [-r RR] [-g TOTAL_GAIN] [-l PREV_LOSS] ENTRY TARGET

Reward to risk calculator. Displays information in the order of how one would
input information into Fidelity Active Trader Pro OTOCO form

positional arguments:
  ENTRY                 objective entry price
  TARGET                target price

options:
  -h, --help            show this help message and exit
  -v, --verbose         verbose logging output (default: False)
  -r, --rr RR           reward to risk ratio as an integer (default: 3)
  -g, --total-gain TOTAL_GAIN
                        total realized gain (default: 300)
  -l, --prev-loss PREV_LOSS
                        previous loss to account for adjusted cost basis
                        (default: None)
```

## Example

If our objective entry is at $30, target is at $40, 1:3 risk/reward with desired total realized gain to be $600, then
```
> python rr.py -g 600 -r 3 30 40
{
    "quantity": 60,
    "limit price buy": "$30.00",
    "limit price sell": "$40.00",
    "stop price loss": "$26.67",
    "total realized gain": "$600.00",
    "total realized loss": "$200.00",
    "ratio": 3,
    "position_size": "$1800.00"
}
```
says, "in the fidelity OTOCO (one triggers a one cancels the other) form, set a limit order to buy 60 shares at $30, set a limit sell order at $40, set a stop loss order at $26.67".

If we get stopped out, want to re-enter the position at 1:2 risk/reward at the previous stop price, same target $40:
```
> python rr.py -g 600 -r 2 -l 200 26.67 40
{
    "quantity": 61,
    "limit price buy": "$26.67",
    "limit price sell": "$40.00",
    "stop price loss": "$24.92",
    "adjusted cost basis": "$29.95",
    "total realized gain": "$613.13",
    "total realized loss": "$306.56",
    "ratio": 2,
    "position_size": "$1826.87"
}
```
says, "in the fidelity OTOCO form, set a limit order to buy 61 shares at $26.67, set a limit sell order at $40, set a stop loss order at $24.92, adjusted cost basis will be $29.95 factoring in a previous loss of $200". This will effectively resume the previous trade that we were whipsawed out of, at a more tolerant risk/reward.

Alternatively, to re-enter the position at 1:3 risk/reward at the previous stop price, same target $40:
```
> python rr.py -g 600 -r 3 -l 200 26.67 40
{
    "quantity": 61,
    "limit price buy": "$26.67",
    "limit price sell": "$40.00",
    "stop price loss": "$26.60",
    "adjusted cost basis": "$29.95",
    "total realized gain": "$613.13",
    "total realized loss": "$204.38",
    "ratio": 3,
    "position_size": "$1826.87"
}
```
says, "in the fidelity OTOCO form, set a limit order to buy 61 shares at $26.67, set a limit sell order at $40, set a stop loss order at $26.60, adjusted cost basis will be $29.95 factoring in a previous loss of $200". This will effectively resume the previous trade that we were whipsawed out of, at the same risk/reward.
