#!/bin/env python3
#Q1
class Tortue:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def localise(self):
      return f'({self.x},{self.y})'
  def avance(self,v,t):
      self.x = v
      self.y = t

ma_tortue = Tortue(5,0)
print(ma_tortue.localise())       # (5,0)
ma_tortue.avance(10,10)
print(ma_tortue.localise())

#Q2
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
      self.X = (random.randint(0,self.vmax),self.X[1])
    else:
        self.X= (v,t)

#ma_tortue = Tortue(5,0)
ma_tortue = Tortue("Samy",(5,0),vmax=10)

print(ma_tortue.localise())       # (5,0)
ma_tortue.avance()
print(ma_tortue.localise())


#!/usr/bin/env python3

#main tortue

from Tortue import Tortue
from Course import Course

la_course = Course()
for t in range(5):
  la_course.enregistre(Tortue(f"tortue{t}",0,0))
la_course.run()
import random

class Tortue:

    def __init__(self,name,x,y,vmax=random.randint(2,8)):
        self.x = x
        self.y = y
        self.name = name
        self.vmax = vmax

    def localise(self):
        return (self.name, self.x, self.y)

    def avance(self):
        self.x += random.randint(0,self.vmax)

#course
from Tortue import Tortue

class Course():
    def __init__(self):
        self.liste = []


    def enregistre(self,T):
        self.liste.append(T)

    def run(self):
        print("1,2,3... Go!")
        for step in range(100):
          print(f"{step=}")
          for t in self.liste:
            t.avance()
            print(t.localise())

