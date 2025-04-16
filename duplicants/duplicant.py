import random

class Duplicant:
    def __init__(self, nom, classe, attaque, defense, vie, soin, stress):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.defense = defense
        self.vie = vie
        self.vie_max = vie  # Ajouter la vie max
        self.soin = soin
        self.stress = stress
        self.experience = 0
        self.niveau = 1
        self.inventaire = []
        self.competences = self.get_competences_de_classe()
        self.equipe = None  # Reference à l'équipe

    def attaquer(self, cible):
        degats = self.attaque - cible.defense
        if degats < 0:
            degats = 0
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.recevoir_degats(degats)  # Utiliser la méthode recevoir_degats de la cible
        print(f"{cible.nom} a maintenant {cible.vie} PV.")

    def defendre(self):
        print(f"{self.nom} se prépare à se défendre!")
        # Logique de défense à ajouter
        pass

    def utiliser_competence(self, competence, cible):
        print(f"{self.nom} utilise {competence['nom']}!")
        degats = self.attaque  # Dégâts de base
        if competence['type'] == 'attaque':
            degats = int(degats * competence['puissance'])
            cible.recevoir_degats(degats)
            print(f"{self.nom} inflige {degats} points de dégâts à {cible.nom}!")
        elif competence['type'] == 'soin':
            soin_montant = int(self.soin * competence['puissance'])
            self.vie += soin_montant
            if self.vie > self.vie_max:
                self.vie = self.vie_max
            print(f"{self.nom} se soigne de {soin_montant} PV!")
        # Ajouter d'autres types de compétences
        return degats

    def recevoir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Classe: {self.classe}, Niveau: {self.niveau}")
        print(f" ATT: {self.attaque}, DEF: {self.defense}, PV: {self.vie}/{self.vie_max}, Stress: {self.stress}")
        print(" Compétences:")
        for comp in self.competences:
            print(f" - {comp['nom']} ({comp['type']}, Puissance: {comp['puissance']})")
        print(" Inventaire:", self.inventaire)

    def gagner_experience(self, experience):
        self.experience += experience
        print(f"{self.nom} gagne {experience} points d'expérience.")
        self.verifier_niveau_up()

    def verifier_niveau_up(self):
        experience_pour_niveau_suivant = 100 * self.niveau
        if self.experience >= experience_pour_niveau_suivant:
            self.niveau_up()

    def niveau_up(self):
        self.niveau += 1
        self.attaque += 5
        self.defense += 3
        self.vie_max += 10
        self.vie = self.vie_max  # Rétablir la vie au max
        self.soin += 1
        print(f"\n{self.nom} passe au niveau {self.niveau}!")

    def get_competences_de_classe(self):
        if self.classe == "Brute":
            return [
                {"nom": "Coup Puissant", "type": "attaque", "puissance": 1.5},
                {"nom": "Cri de Guerre", "type": "buff", "puissance": 1.2}
            ]
        elif self.classe == "Eclaireur":
            return [
                {"nom": "Tir Rapide", "type": "attaque", "puissance": 1.2},
                {"nom": "Camouflage", "type": "buff", "puissance": 1.1}
            ]
        elif self.classe == "Ingenieur":
            return [
                {"nom": "Grenade", "type": "attaque", "puissance": 1.4},
                {"nom": "Soin Rapide", "type": "soin", "puissance": 1.3}
            ]
        elif self.classe == "Chimiste":
            return [
                {"nom": "Jet Acide", "type": "attaque", "puissance": 1.3},
                {"nom": "Stimulant", "type": "soin", "puissance": 1.2}
            ]
        else:
            return []