# def multiple_arg(*args):
#     print(args)
#     pass

# def multiple_kwargs(**kwargs):
#     print(kwargs)
#     pass

# multiple_arg(1, 2, 10)
# multiple_kwargs(firstname="ihab", lastname="abadi")

# fct1 = lambda x : x**2
# def fct2(x) :
#     return x**2
# print(fct1(2))
# print(type(fct1))
# print(fct2(2))
# print(type(fct2))

# t = ["bonjour","dix","cailloux", "aaa"]

# def ma_fonction_filtre(t):
#     return t[0] == 'a'

# print(list(filter(lambda t: t[0] == 'a', t)))

# ## Liste

# fruits = ["pomme", "banane"]

# set_fruits = set()
# set_fruits.add("pomme")
# set_fruits.add("pomme")
# set_fruits.add("pomme")

# print(set_fruits)

# ## Liste => Stack (pile)

# pile = []
# pile.append("premier")
# pile.append("deuxieme")
# pile.pop()

# from collections import deque

# file = deque(["client1", "client2"])
# file.append("client3")
# file.popleft()

class CompteBancaire:

    # compteur = 0

    # def __new__(cls):
    #     cls.compteur = cls.compteur + 1
    
    def __add__(self, autre):
        return CompteBancaire(self.titulaire + " et " + autre.titulaire, self.solde + autre.solde)
    
    def __repr__(self):
        return f"Titulaire : {self.titulaire}, Solde : {self.solde} €"
        

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.__solde = solde 

    @property
    def solde(self):
        return self.__solde
    
    @solde.setter
    def solde(self, montant):
        if montant >= 0:
            self.__solde = montant
        else:
            raise ValueError("Le montant doit être positif")

compte1 = CompteBancaire("Alice", 100)
compte2 = CompteBancaire("Bob", 100)
print((compte1 + compte2))
# compte.__solde = 200
# # compte.solde = 200
# # print(compte.solde)
# # compte.solde = -100
# print(compte.solde)

from abc import ABC

class Vehicule(ABC):
    def demarrer(self):
        print("Véhicule démarrée")

class Electrique:
    def charger_batterie(self):
        print("Batterie en charge")
    
    def demarrer(self):
        print("Véhicule Electrique démarrée")

class VoitureElectrique(Vehicule, Electrique):
    def demarrer(self):
        super().demarrer()
        print("Voiture démarrée")

v1 = VoitureElectrique()
v1.demarrer()

class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être surchargée")

class Chien(Animal):
    def parler(self):
        print("Woof")

class Chat(Animal):
    def parler(self):
        print("Meow")


animaux = [Chien(), Chat()]
print(type(animaux))
for animal in animaux:
    print(type(animal))
    animal.parler() 
