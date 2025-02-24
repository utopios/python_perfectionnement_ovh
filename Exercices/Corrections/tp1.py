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

## Question 3 Version Nicolas

def ajouter_client(nom):
    if nom not in clients:
        clients[nom]=set()

# def passer_commande(nom, *args, **kwargs) -> bool:
#     if nom not in clients:
#         raise NameError("Le nom n'existe pas")
    
#     total = 0
#     for service in args:
#         total += service.calculer_prix()
    
#     if 'remise' in kwargs:
#         total *= 0.9
#     if 'urgent' in    kwargs:
#         total *= 1.2
    
#     commande = {'client':nom, 'services': args, 'options': kwargs, 'total': total}

#     commandes_en_attente.append(commande)
#     clients[nom].append(commande)
#     return True

    


# ajouter_client("nicolas")

# print(f'tous les clients: {clients}')

# s1 = Serveur('srv1',1,2,1)
# c1 = Cloud('cld1',1) 
# d1 = Domaine('toto.re',2,'.com')
# passer_commande("nicolas", s1, c1, d1, remise= True, urgent= False)

# print(f'toutes les commandes: {commandes_en_attente}')

## Question 3 Version Ihab

def passer_commande(client, *services, **options):
    total = sum(service.calculer_prix() for service in services)
    
    if options.get("remise"):
        total *= (1 - options["remise"] / 100)

    if options.get("urgent"):
        total += 20
    
    commande = {
        "client": client,
        "services": [service.nom for service in services],
        "total": round(total, 2),
        "options": options
    }
    
    commandes_en_attente.append(commande)
    clients[client].append(deepcopy(commande))
    print(f"Commande ajoutée pour {client}: {commande}")

## Question 4

from functools import reduce

def generer_factures():
    montants = list(map(lambda c:c['total'], commande_en_attente))
    commandes_importantes = list(filter(lambda c: c['total'] > 100, commande_en_attente))
    total_general = reduce(lambda acc, val: acc + val, montants, 0)

    print("\n Commandes dépassant 100 euros ")
    for commande in commandes_importantes:
        print(commande)
    
    print(f"\n Montant total de toutes les commandes {total_general} €")


def afficher_historique(client):
    print(f"\nHistorique des commandes pour {client}:")
    for commande in clients[client]:
        print(commande)