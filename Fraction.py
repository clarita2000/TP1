#!/bin/env python3
import math
class Fraction:
  def __init__(self,x,y):
      if y==0:
          raise Exception("denominateur nul")
      p=math.gcd(int(x),int(y))
      self.x= x//p
      self.y= y//p

  def __str__(self):
      if self.x == 0:
            return f"0"
      if self.x/self.y < 0:
          if abs(self.y)== 1:
              return f"-{abs(self.x)}"
          return f"-{abs(self.x)}/{abs(self.y)}"
      if abs(self.y) == 1:
          return f"{abs(self.x)}"
      return f"{abs(self.x)}/{abs(self.y)}"

  def inverse(self):
      f=Fraction(self.y,self.x)
      return f

if __name__=="__main__":
    f = Fraction(15,27)
    print(f)                  # 15/27
    f2 = f.inverse()
    print(f2)                 # 27/15

    print(Fraction(2,3))     # écrit 2/3
    print(Fraction(-2,3))    # écrit -2/3
    print(Fraction(2,-3))    # écrit -2/3
    print(Fraction(-2,-3))   # écrit 2/3
    print(Fraction(2,1))     # écrit 2
