#!/bin/env python3
from TictacToe import TictacToe
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
