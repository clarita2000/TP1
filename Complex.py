#!/bin/env python3
import math

class Complex:
    def initialise(z,reel,imag):
        z.x = reel
        z.y = imag

    def module(z):
        return math.sqrt(z.x**2 + z.y**2)

    def argument(z):
        return math.atan(z.y/z.x)

if __name__=="__main__":
    pass
