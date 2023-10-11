#!/bin/env python3
from Complexe import Complexe

def module(z):
  return math.sqrt(z.x**2 + z.y**2)

def argument(z):
  return math.atan(z.y/z.x)

z1 = Complexe()
z2 = Complexe()

z1.initialise(1,2)
z2.initialise(2,-1)

print(z1,z2)          # <__main__.Complex object at 0x7fdfec643130>
print(z1.module())
print(z2.argument())


#!/bin/env python3
from Complexe import Complexe
z1= Complexe()
z1.initialise(1,2)

z2=z1.conjugue()
print(f"z1={z1.x},{z1.y}")
print(f"z2={z2.x},{z2.y}")
