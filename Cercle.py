#!/bin/env python3
from math import pi

class Cercle:
    def initRayon(self,r):
        self.rayon = r

    def circonference(self):
        return 2*self.rayon*pi

    def surface(self):
        return self.rayon**2 * pi
