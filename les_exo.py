Exercice 1

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
    if self.classe == "A":
        self.reseau = self.a
    elif self.classe == "B":
        self.reseau = self.a,self.b
    elif self.classe == "C" :
        self.reseau = self.a,self.b,self.c
    return self.reseau



  def equipement(self):
    if self.classe == "A":
        self.reseau = self.b,self.c,self.d
    elif self.classe == "B":
        self.reseau = self.c,self.d
    elif self.classe == "C":
        self.reseau = self.d
    return self.reseau

if __name__=="__main__":
  ip1 = IPaddress(192,168,1,1)
  ip2 = IPaddress(172,20,21,19)
  ip3 = IPaddress(10,1,1,1)

  print(f"{ip1.classe()=}")
  print(f"{ip2.classe()=}")
  print(f"{ip3.classe()=}")

  print(f"{ip1.reseau()=}")
  print(f"{ip2.reseau()=}")
  print(f"{ip3.reseau()=}")

  print(f"{ip1.equipement()=}")
  print(f"{ip2.equipement()=}")
  print(f"{ip3.equipement()=}")

#_____________________
#Exo 2

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

#EXO3
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



#exo4
#!/usr/bin/env python3


from Tortue import Tortue
from Course import Course



la_course = Course()
for t in range(5):
  la_course.enregistre(Tortue(f"tortue{t}",0,0))
la_course.run()

#
