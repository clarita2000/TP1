#!/bin/env python3
#exo 3
from collections import defaultdict

class Frigo:
    def __init__(self):
        self.contenu = defaultdict(int)

    def depose(self,panier):
        for k in panier:
            self.contenu[k] += panier[k]

    def disponible(self,panier):
        for k in panier:
            if not k in self.contenu:
                return False
            if self.contenu[k] < panier[k]:
                return False
        return True

    def retire(self,panier):
        for k in panier:
            if not k in self.contenu:
                raise Exception("impossible")
            if self.contenu[k] < panier[k]:
                raise Exception("impossible")
            self.contenu[k] -= panier[k]

    def etat(self):
        print("---")
        for k in self.contenu:
            print(f"{k}: {self.contenu[k]}")
        print("---")

class Recette:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def possible(self,frigo):
        return frigo.disponible(self.ingredients)

if __name__=="__main__":
    un_frigo = Frigo()
    un_frigo.etat()
    un_frigo.depose({
            "oeufs": 6
            , "beurre": 250
            , "yaourt": 6
            , "fraise": 10
            })
    un_frigo.etat()
    un_frigo.depose({
            "oeufs": 12
            , "beurre": 250
            , "yaourt": 6
            , "prunes": 4
            })
    un_frigo.etat()

    une_tarte = Recette({
            "oeufs": 2
            , "beurre": 100
    })

    print(une_tarte.possible(un_frigo))
