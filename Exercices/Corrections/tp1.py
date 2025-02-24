from abc import ABC, abstractmethod
from collections import deque


## Version Sebastien

# class Service(ABC):      
#     @abstractmethod
#     def calculer_prix(self):
#         pass

# class Serveur(Service):
#     def __init__(self, prix):
#         self.prix = prix

#     def calculer_prix(self):
#         return self.prix

# class Cloud(Service):
#     def __init__(self, prix):
#         self.prix = prix

#     def calculer_prix(self):
#         return self.prix

# class Domaine(Service):
#     def __init__(self, prix):
#         self.prix = prix

#     def calculer_prix(self):
#         return self.prix

## Version Ihab 

class Service(ABC):
    def __init__(self, nom, base_prix):
        self.nom = nom
        self.base_prix = base_prix

    @abstractmethod
    def calculer_prix(self):
        pass

class Serveur(Service):
    def __init__(self, nom, base_prix, cpu, ram):
        super().__init__(nom, base_prix)
        self.cpu = cpu
        self.ram = ram

    def calculer_prix(self):
        return self.base_prix + (self.cpu * 10) + (self.ram * 5)

class Cloud(Service):
    def __init__(self, nom, base_prix, stockage):
        super().__init__(nom, base_prix)
        self.stockage = stockage

    def calculer_prix(self):
        return self.base_prix + (self.stockage * 2)

class Domaine(Service):
    def __init__(self, nom, base_prix, extension):
        super().__init__(nom, base_prix)
        self.extension = extension

    def calculer_prix(self):
        return self.base_prix + (10 if self.extension == ".com" else 5)

## Question 2

clients = {
    #"Alice" : set()
}

commande_en_attente = deque()