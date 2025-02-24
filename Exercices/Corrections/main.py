from tp1_version2 import PlateformeServices, Serveur, Cloud, Domaine
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

print(__name__)