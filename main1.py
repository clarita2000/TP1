#!/bin/env python3
from Complexe import Complexe
z1= Complexe()
z1.initialise(1,2)

z2=z1.conjugue()
print(f"z1={z1.x},{z1.y}")
print(f"z2={z2.x},{z2.y}")
