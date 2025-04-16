class Creature:
    def __init__(self, nom, niveau, type, attaque, defense, vie):
        self.nom = nom
        self.niveau = niveau
        self.type = type
        self.attaque = attaque
        self.defense = defense
        self.vie = vie

    def attaquer(self, cible):
        # Logique d'attaque de la créature (à améliorer)
        degats = self.attaque - cible.defense
        if degats < 0:
            degats = 0
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        cible.vie -= degats
        if cible.vie < 0:
            cible.vie = 0
        print(f"{cible.nom} a maintenant {cible.vie} PV.")

    def defendre(self):
        # Logique de défense de la créature (à améliorer)
        print(f"{self.nom} se prépare à se défendre!")
        pass