# RR

## Description

simple reward to risk calculator

## Usage

```
usage: rr.py [-h] [-p POSITION_SIZE] BUY STOP SELL

calculates reward to risk

positional arguments:
  BUY                   purchase price. This accepts expressions
  STOP                  stop loss. This accepts expressions
  SELL                  price target. This accepts expressions

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

# Expressions are allowed, for example for the STOP argument
$ python3 rr.py 37 "33-1" 52 -p 1000  
position_size=$1000.0
shares=27
ratio=3.00
gain=$405.00
loss=$135.00 
```
