#!/bin/env python3
class adresseIP:
  def __init__(self,a,b,c,d):
      self.a= a
      self.b= b
      self.c= c
      self.d= d

  def classe(self):
    if self.a & 0b10000000 == 0b00000000:
        self.classe = "A"
    elif self.a & 0b11000000 == 0b10000000:
        self.classe = "B"
    elif self.a & 0b11100000 ==0b11000000:
        self.classe = "C"
    return self.classe

  def reseau(self):
    if self.a & 0b10000000 == 0b00000000:
        self.reseau = self.a
    elif self.a & 0b11000000 == 0b10000000:
        self.reseau = self.a,self.b
    elif self.a & 0b11100000 ==0b11000000:
        self.reseau = self.a,self.b,self.c
    return self.reseau


  def adresseEQ(self):
      if self.a & 0b10000000 == 0b00000000:
        self.adresseEQ = self.b,self.c,self.d
      elif self.a & 0b11000000 == 0b10000000:
        self.adresseEQ = self.c,self.d
      elif self.a & 0b11100000 ==0b11000000:
        self.adresseEQ = self.d
      return self.adresseEQ


if __name__=="__main__":
    ip1 = adresseIP(192,168,1,1)
    ip2 = adresseIP(172,168,21,19)
    ip3 = adresseIP(10,1,1,1)

    re1 = ip1.reseau()
    re2 = ip2.reseau()
    re3 = ip3.reseau()

    eq1 = ip1.adresseEQ()
    eq2 = ip2.adresseEQ()
    eq3 = ip3.adresseEQ()

    print(f"{ip1.classe()=}")
    print(f"{ip2.classe()=}")
    print(f"{ip3.classe()=}")

    print(f"{re1=}")
    print(f"{re2=}")
    print(f"{re3=}")

    print(f"{eq1=}")
    print(f"{eq2=}")
    print(f"{eq3=}")
