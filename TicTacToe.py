#!/bin/env python3
class TicTacToe:
    def __init__(self):
        self.damier = {}
        for i in (1,2,3):
            for j in (1,2,3):
                self.damier[(i,j)] = "[]"
    def __str__(self):
        s=""
        for i in (1,2,3):
            for j in (1,2,3):
                s+=self.damier[(i,j)]
            s+="\n"
        return s

    def place(self,x,y,p):
        self.damier[(x,y)] = p

damier = TicTacToe()
print(damier)

damier.place(1,1,'0')
print(damier)

damier.place(2,3,'X')
print(damier)

class Joueur:
    def __init__(self,nom,pion):
        self.nom= nom
        self.pion= pion

    def __str__(self):
        return f"{self.damier}, {self.nom}, {self.pion} "

damier = TicTacToe()
bob = Joueur(damier,nom='Bob',pion='X')
alice = Joueur(damier,nom='Alice',pion='O')
print(damier)

