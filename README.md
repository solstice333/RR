# RR

## Description

simple reward to risk calculator

## Usage

```
usage: rr.py [-h] [-p POSITION_SIZE] BUY SELL STOP

calculates reward to risk

positional arguments:
  BUY                   purchase price
  SELL                  price target
  STOP                  stop loss

optional arguments:
  -h, --help            show this help message and exit
  -p POSITION_SIZE, --position-size POSITION_SIZE
                        total value of position. Defaults to $1000
```

## Example

```
$ python3 rr.py 17.22 24.22 15.22
position_size=$1000
shares=58
ratio=3.50
gain=$406.0
loss=$115.9999999999999
```
