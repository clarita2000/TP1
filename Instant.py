#!/bin/env python3
class Instant:
  def __init__(self,h=0,m=0,s=0):
      self.h= h
      self.m= m
      self.s= s
      self.conversion()

  def __str__(self):
      s = []
      if self.h!=0: s += [f"{self.h}h"]
      if self.m!=0: s += [f"{self.m}m"]
      if self.s!=0: s += [f"{self.s}s"]
      return " ".join(s)

  def conversion(self):
      self.h= self.s//3600
      self.s %= 3600
      self.m= self.s//60
      self.s %= 60

if __name__=="__main__":
    instant1 = Instant(h=1,m=10,s=30)
    print(instant1)      # 1h 10mn 30s

    instant2 = Instant(m=10,s=30)
    print(instant2)      # 10mn 30s

    instant3 = Instant(m=10)
    print(instant3)      # 10mn

    instant4 = Instant(h=1,m=90)
    print(instant4)      # 2h 30mn
