#!/bin/env python3
import random
class Tortue:
  def __init__(self,nom,X,vmax=random.randint(2,10)):
      self.nom = nom
      self.X = X
      self.vmax= vmax
  def localise(self):
      return f'({self.nom}, {self.X})'

  def avance(self,v="pa",t="ba"):
    if v=="pa" and t=="ba":
      self.X = (random.randint(0,self.vmax), self.X[1])
    else:
        self.X = (v,t)

tortues = []   # tortues au départ
for t in range(5):
  tortues.append(Tortue(f"tortue{t}",(0,0)))

print("1, 2, 3 partez !")
for step in range(10):
  print(f"{step=}")
  for t in tortues:
    t.avance()
    print(t.localise())


#ma_tortue = Tortue(5,0)
#ma_tortue = Tortue("Samy",(5,2),vmax=10)
#print(ma_tortue.localise())       # (5,0)
#ma_tortue.avance(10,10)
#print(ma_tortue.localise())

