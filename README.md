# RR

## Description

simple reward to risk calculator

## Usage

```
usage: rr.py [-h] [-p POSITION_SIZE] BUY STOP SELL

calculates reward to risk

positional arguments:
  BUY                   purchase price
  STOP                  stop loss
  SELL                  price target

optional arguments:
  -h, --help            show this help message and exit
  -p POSITION_SIZE, --position-size POSITION_SIZE
                        total value of position. Defaults to $1000
```

## Example

```
$ python3 rr.py 17.22 15.22 24.22 
position_size=$1000
shares=58
ratio=3.50
gain=$406.0
loss=$116.00

# I like to put the stuff that I modify frequently at the end of the argument list. 
# For example the sell price target
$ python3 rr.py 17.22 15.22 -p 2e3 24.22 
position_size=$2000.0
shares=116
ratio=3.50
gain=$812.0
loss=$232.00
```
