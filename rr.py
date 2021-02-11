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
   def __init__(self, *, sz: float, rr: int) -> None:
      self._sz = sz
      self._rr = rr

   def rewrisk(self, *, entry: float, target: float) -> RewRiskData:
      shares = int(self._sz / entry)
      dist = (target - entry)/self._rr
      stop = entry - dist
      return RewRiskData(
         position_size=self._sz, 
         ratio=self._rr,
         shares=shares, 
         stop=stop,
         gain=(target - entry)*shares,
         loss=(entry - stop)*shares,
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
   parser.add_argument("-r", "--rr",
      default=3,
      help="reward to risk ratio as an integer. Defaults to 3",
      type=int)
   parser.add_argument("ENTRY", 
      help="purchase price. This accepts expressions", type=floatify)
   parser.add_argument("TARGET", 
      help="price target. This accepts expressions", type=floatify)
   args = parser.parse_args()

   rr = RewRiskCalc(sz=args.position_size, rr=args.rr)
   print(fmt_rr_data(rr.rewrisk(entry=args.ENTRY, target=args.TARGET)))

if __name__ == '__main__': main()
