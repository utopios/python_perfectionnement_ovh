from abc import ABC, abstractmethod
from collections import deque
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


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.commandes = set()

    def ajouter_commande(self, commande):
        self.commandes.add(commande)

    def afficher_historique(self):
        print(f"\nHistorique des commandes pour {self.nom}:")
        for commande in self.commandes:
            print(commande)


class Commande:
    def __init__(self, client, services, **options):
        self.client = client
        self.services = services
        self.options = options
        self.total = self.calculer_total()

    def calculer_total(self):
        total = sum(service.calculer_prix() for service in self.services)

        if self.options.get("remise"):
            total *= (1 - self.options["remise"] / 100)

        if self.options.get("urgent"):
            total += 20  # Frais supplémentaire pour l'urgence

        return round(total, 2)

    def __str__(self):
        services_str = ", ".join(service.nom for service in self.services)
        return f"Client: {self.client.nom}, Services: [{services_str}], Total: {self.total} €, Options: {self.options}"


class PlateformeServices:
    def __init__(self):
        self.clients = {}
        self.commandes_en_attente = []

    def ajouter_client(self, nom):
        client = Client(nom)
        self.clients[nom] = client
        return client

    def passer_commande(self, client_nom, *services, **options):
        client = self.clients.get(client_nom)
        if not client:
            print(f"Client {client_nom} non trouvé.")
            return

        commande = Commande(client, services, **options)
        self.commandes_en_attente.append(commande)
        client.ajouter_commande(commande)
        print(f"Commande ajoutée pour {client.nom}: {commande}")

    def generer_factures(self):
        print("\n--- Factures générées ---")
        montants = list(map(lambda c: c.total, self.commandes_en_attente))
        commandes_importantes = list(filter(lambda c: c.total > 100, self.commandes_en_attente))

        for commande in self.commandes_en_attente:
            print(commande)

        print("\nCommandes dépassant 100 €:")
        for commande in commandes_importantes:
            print(commande)

        total_general = sum(montants)
        print(f"\nMontant total de toutes les commandes: {total_general} €")

    def afficher_historique_client(self, client_nom):
        client = self.clients.get(client_nom)
        if client:
            client.afficher_historique()
        else:
            print(f"Client {client_nom} non trouvé.")


plateforme = PlateformeServices()
# Ajout de clients
alice = plateforme.ajouter_client("Alice")
bob = plateforme.ajouter_client("Bob")

# Création de services
serveur1 = Serveur("Serveur Pro", 100, cpu=4, ram=16)
cloud1 = Cloud("Cloud Basic", 50, stockage=100)
domaine1 = Domaine("Site Web", 20, ".com")

# Passer des commandes
plateforme.passer_commande("Alice", serveur1, cloud1, remise=10, urgent=True)
plateforme.passer_commande("Bob", domaine1, cloud1)
plateforme.passer_commande("Alice", domaine1, serveur1, remise=5)

# Générer les factures
plateforme.generer_factures()

# Afficher l'historique des commandes
plateforme.afficher_historique_client("Alice")
plateforme.afficher_historique_client("Bob")