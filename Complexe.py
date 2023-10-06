#!/bin/env python3
import math

class Complexe:
  def initialise(z,reel,imag):
    z.x = reel
    z.y = imag

  def module(z):
    return math.sqrt(z.x**2 + z.y**2)

  def argument(z):
    return math.atan(z.y/z.x)

  def conjugue(self):
      nouveau=Complexe()
      nouveau.x = self.x
      nouveau.y = -self.y
      return nouveau


if __name__=="__main__":
    pass
