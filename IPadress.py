#!/bin/env python3

class IPaddress:
  def __init__(self,a,b,c,d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d

  def classe(self):
    if self.a & 0b10000000 == 0b00000000:
        self.classe = "A"
    elif self.a & 0b11000000 == 0b10000000:
        self.classe = "B"
    elif self.a & 0b11100000 ==0b11000000:
        self.classe = "C"

    return self.classe

  def reseau(self):
    pass

  def equipement(self):
    pass

if __name__=="__main__":
  ip1 = IPaddress(192,168,1,1)
  ip2 = IPaddress(172,20,21,19)
  ip3 = IPaddress(10,1,1,1)

  print(f"{ip1.classe()=}")
  print(f"{ip2.classe()=}")
  print(f"{ip3.classe()=}")
