import random
from combat import attack

def handle_combat(duplicants, creature):
    print("\n--- Début du Combat ---")
    while creature.vie > 0 and any(dup.vie > 0 for dup in duplicants):
        for attaquant in duplicants + [creature]:
            if attaquant.vie <= 0:
                continue  # Si la créature ou le Duplicant est mort, il ne peut pas attaquer
            if attaquant in duplicants:
                cible = creature
                attack.attack(attaquant, cible)
            else:
                cible = random.choice([dup for dup in duplicants if dup.vie > 0])
                attack.attack(attaquant, cible)
            if creature.vie <= 0:
                print(f"\n{creature.nom} est vaincu!")
                break
            if any(dup.vie <= 0 for dup in duplicants):
               print("\nUn Duplicant est vaincu!")
               break
    print("\n--- Fin du Combat ---")