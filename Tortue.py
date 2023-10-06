#!/bin/env python3
import random
class Tortue:
  def __init__(self,nom,X,vmax):
      self.nom = nom
      self.X = X
      self.vmax = random.randint(2,10)

  def localise(self):
      return f'({self.nom}, {self.X})'

  def avance(self,v="pa",t="ba"):
    if v=="pa" and t=="ba":
      self.X = (random.randint(0,self.vmax), self.X[1])
    else:
        self.X = (v,t)

#ma_tortue = Tortue(5,0)
ma_tortue = Tortue("Samy",(5,2),vmax=10)
print(ma_tortue.localise())       # (5,0)
ma_tortue.avance(10,10)
print(ma_tortue.localise())

