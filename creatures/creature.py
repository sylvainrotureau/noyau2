import random

class Creature:
    def __init__(self, nom, niveau, type, attaque, defense, vie):
        self.nom = nom
        self.niveau = niveau
        self.type = type
        self.attaque = attaque
        self.defense = defense
        self.vie = vie
        self.experience_donnee = niveau * 15 # XP donné à la mort

    def attaquer(self, cible):
        degats = self.attaque - cible.defense
        if degats < 0:
            degats = 0
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.vie -= degats
        if cible.vie < 0:
            cible.vie = 0
        print(f"{cible.nom} a maintenant {cible.vie} PV.")

    def defendre(self):
        print(f"{self.nom} se prépare à se défendre!")
        # Logique de défense à ajouter
        pass

    def utiliser_competence(self, cible):
        # Logique de compétence de la créature (si les créatures ont des compétences)
        pass

    def recevoir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

    def afficher_infos(self):
        print(f"\n{self.nom} (Niveau {self.niveau}, Type {self.type})")
        print(f"  ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}")