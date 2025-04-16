import random

class Duplicant:
    def __init__(self, nom, classe, attaque, defense, vie, soin, stress):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.defense = defense
        self.vie = vie
        self.soin = soin
        self.stress = stress
        self.experience = 0
        self.niveau = 1
        self.inventaire = []
        self.competences = self.get_competences_de_classe()

    def attaquer(self, cible):
        # Logique d'attaque du Duplicant (à améliorer)
        degats = self.attaque - cible.defense
        if degats < 0:
            degats = 0
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.vie -= degats
        if cible.vie < 0:
            cible.vie = 0
        print(f"{self.nom} a maintenant {cible.vie} PV.")

    def defendre(self):
        # Logique de défense du Duplicant (à améliorer)
        print(f"{self.nom} se prépare à se défendre!")
        pass

    def utiliser_competence(self, competence, cible):
        # Logique d'utilisation des compétences (à implémenter)
        print(f"{self.nom} utilise {competence['nom']}!")
        degats = self.attaque  # Exemple : les compétences font les dégâts de l'attaque de base
        if competence['type'] == 'attaque':
           degats = int(degats * competence['puissance'])
           cible.vie -= degats
           print(f"{self.nom} inflige {degats} points de dégâts à {cible.nom}!")
        return degats

    def get_competences_de_classe(self):
        if self.classe == "Brute":
            return [
                {"nom": "Frappe puissante", "type": "attaque", "puissance": 2.0, "effet": None},
            ]
        elif self.classe == "Eclaireur":
            return [
                {"nom": "Tir rapide", "type": "attaque", "puissance": 1.0, "effet": "defense_baisse"},
            ]
        elif self.classe == "Ingenieur":
            return [
                {"nom": "Construire tourelle", "type": "autre", "puissance": 0, "effet": None},
            ]
        elif self.classe == "Chimiste":
            return [
                {"nom": "Jet acide", "type": "attaque", "puissance": 1.5, "effet": "attaque_baisse"},
            ]
        else:
            return []

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Classe: {self.classe}, Niveau: {self.niveau}")
        print(f" ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}, SOI: {self.soin}, STR: {self.stress}")
        print(f" Inventaire: {', '.join(self.inventaire) if self.inventaire else 'Vide'}")
        print(" Compétences:")
        if self.competences:
            for i, competence in enumerate(self.competences):
                print(f"   {i + 1}. {competence['nom']} ({competence['type']})")
        else:
            print("   Aucune")

    def gagner_experience(self, xp):
        self.experience += xp
        print(f"{self.nom} gagne {xp} points d'expérience!")
        self.verifier_niveau_up()

    def verifier_niveau_up(self):
        niveau_suivant = 100 * self.niveau  # Exemple : 100 XP par niveau
        if self.experience >= niveau_suivant:
            self.niveau_up()

    def niveau_up(self):
        self.niveau += 1
        self.attaque += random.randint(1, 3)
        self.defense += random.randint(1, 2)
        self.vie += random.randint(5, 10)
        self.soin += random.randint(0, 2)
        self.stress -= random.randint(0, 5)  # Réduire le stress au niveau up
        print(f"\n{self.nom} monte au niveau {self.niveau}!")
        print(f"Ses statistiques augmentent!")
        self.afficher_infos()