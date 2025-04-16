def attack(attacker, defender):
    # Logique d'attaque de base (à améliorer)
    degats = attacker.attaque - defender.defense
    if degats < 0:
        degats = 0
    print(f"{attacker.nom} attaque {defender.nom} et inflige {degats} dégâts.")
    defender.vie -= degats
    if defender.vie < 0:
        defender.vie = 0
    print(f"{defender.nom} a maintenant {defender.vie} PV.")