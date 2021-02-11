# RR

## Description

simple reward to risk calculator

## Usage

```
usage: rr.py [-h] [-p POSITION_SIZE] [-r RR] ENTRY TARGET

calculates reward to risk

positional arguments:
  ENTRY                 purchase price. This accepts expressions
  TARGET                price target. This accepts expressions

optional arguments:
  -h, --help            show this help message and exit
  -p POSITION_SIZE, --position-size POSITION_SIZE
                        total value of position. Defaults to $1000
  -r RR, --rr RR        reward to risk ratio as an integer. Defaults to 3
```

## Example

```
python3 rr.py -r 3 15.70 16.24 -p 9e3 
position_size=$9000.0
shares=573
ratio=3.00
gain=$309.42
loss=$103.14
stop=$15.52
target=$16.24
```
