#!python3
import argparse
import sys

from typing import NamedTuple

class RewRiskData(NamedTuple):
   position_size: float
   shares: int
   ratio: float
   gain: float
   loss: float
   stop: float
   target: float

class RewRiskCalc:
   def __init__(self, sz: float) -> None:
      self._sz = sz

   @property
   def sz(self) -> float:
      return self._sz

   @sz.setter
   def sz(self, val: float) -> None:
      self._sz = val 

   def rewrisk(self, entry: float, stop: float, target: float) -> RewRiskData:
      shares = int(self._sz / entry)
      return RewRiskData(
         position_size=self._sz, 
         shares=shares, 
         ratio=(target - entry) / (entry - stop),
         gain=(target - entry)*shares,
         loss=(entry - stop)*shares,
         stop=stop,
         target=target
      )

def fmt_rr_data(data: RewRiskData) -> str:
   return f"position_size=${data.position_size}" +\
      f"\nshares={data.shares}" + \
      f"\nratio={data.ratio:.2f}" + \
      f"\ngain=${data.gain:.2f}" + \
      f"\nloss=${data.loss:.2f}" + \
      f"\nstop=${data.stop:.2f}" + \
      f"\ntarget=${data.target:.2f}"

def floatify(expr: str) -> float:
   return float(eval(expr))

def main() -> None:
   parser = argparse.ArgumentParser(description="calculates reward to risk")
   parser.add_argument("-p", "--position-size", 
      default=1000,
      help="total value of position. Defaults to $1000", 
      type=float
   )
   parser.add_argument("ENTRY", 
      help="purchase price. This accepts expressions", type=floatify)
   parser.add_argument("STOP", 
      help="stop loss. This accepts expressions", type=floatify)
   parser.add_argument("TARGET", 
      help="price target. This accepts expressions", type=floatify)
   args = parser.parse_args()

   rr = RewRiskCalc(args.position_size)
   print(fmt_rr_data(rr.rewrisk(args.ENTRY, args.STOP, args.TARGET)))

if __name__ == '__main__':
   main()
