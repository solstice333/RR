# RR

## Description

Reward to risk calculator. Displays information in the order of how one would input information into Fidelity Active Trader Pro OTOCO form

## Usage

```
usage: rr.py [-h] [-r RR] [-g GAIN_TARGET] ENTRY TARGET

calculates reward to risk

positional arguments:
  ENTRY                 purchase price. This accepts expressions
  TARGET                price target. This accepts expressions

options:
  -h, --help            show this help message and exit
  -r RR, --rr RR        reward to risk ratio as an integer. Defaults to 3
  -g GAIN_TARGET, --gain-target GAIN_TARGET
                        gain target
```

## Example

```
PS C:\Users\knavero\Dropbox\python_workspace\RR> python .\rr.py -g 900 -r 3 10.60 11.02                                       
RewardRiskData(shares=2143,
               entry='$10.60',
               target='$11.02',
               stop='$10.46',
               gain='$900.06',
               loss='$300.02',
               position_size='$22715.80',
               ratio=3)
```
