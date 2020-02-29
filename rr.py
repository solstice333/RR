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

class RewRiskCalc:
   def __init__(self, sz: float) -> None:
      self._sz = sz

   @property
   def sz(self) -> float:
      return self._sz

   @sz.setter
   def sz(self, val: float) -> None:
      self._sz = val 

   def rewrisk(self, buy: float, sell: float, stop: float) -> RewRiskData:
      shares = int(self._sz / buy)
      return RewRiskData(
         position_size=self._sz, 
         shares=shares, 
         ratio=(sell - buy) / (buy - stop),
         gain=(sell - buy)*shares,
         loss=(buy - stop)*shares
      )

def fmt_rr_data(data: RewRiskData) -> str:
   return f"position_size=${data.position_size}" +\
      f"\nshares={data.shares}" +\
      f"\nratio={data.ratio:.2f}" +\
      f"\ngain=${data.gain}" +\
      f"\nloss=${data.loss:.2f}"

def main() -> None:
   parser = argparse.ArgumentParser(description="calculates reward to risk")
   parser.add_argument("-p", "--position-size", 
      default=1000,
      help="total value of position. Defaults to $1000", 
      type=float
   )
   parser.add_argument("BUY", help="purchase price", type=float)
   parser.add_argument("SELL", help="price target", type=float)
   parser.add_argument("STOP", help="stop loss", type=float)
   args = parser.parse_args()

   rr = RewRiskCalc(args.position_size)
   print(fmt_rr_data(rr.rewrisk(args.BUY, args.SELL, args.STOP)))

if __name__ == '__main__':
   main()
