import random

def update_creature_behavior(creatures, duplicants, carte):
    # Logique d'IA des créatures
    for creature in creatures:
        if creature.vie <= 0:
            continue

        action = choisir_action(creature, duplicants, carte)

        if action == "attaquer":
            cible = choisir_cible(creature, duplicants)
            if cible:
                creature.attaquer(cible)
        elif action == "deplacer":
            direction = choisir_direction(creature, carte)
            if direction:
                deplacer_creature(creature, direction, carte)
        # Ajouter d'autres actions si nécessaire
        
def choisir_action(creature, duplicants, carte):
    # Logique pour choisir entre attaquer, se déplacer, etc.
    if duplicants:
        return "attaquer"
    else:
        return "deplacer"

def choisir_cible(creature, duplicants):
    # Logique pour choisir la cible de l'attaque
    cibles_en_vie = [dup for dup in duplicants if dup.vie > 0]
    if cibles_en_vie:
        return random.choice(cibles_en_vie)
    else:
        return None

def choisir_direction(creature, carte):
    # Logique pour choisir une direction de déplacement
    salle_actuelle = carte["salles"][creature.position]
    directions_possibles = salle_actuelle["connections"]
    if directions_possibles:
        return random.choice(directions_possibles)
    else:
        return None

def deplacer_creature(creature, direction, carte):
    # Logique pour déplacer la créature
    creature.position = direction
    print(f"{creature.nom} se déplace vers {direction}.")