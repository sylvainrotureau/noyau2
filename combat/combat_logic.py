import random
from combat import attack

def handle_combat(duplicants, creature):
    print("\n--- Début du Combat ---")
    while creature.vie > 0 and any(dup.vie > 0 for dup in duplicants):
        for attaquant in duplicants + [creature]:
            if attaquant.vie <= 0:
                continue
            if attaquant in duplicants:
                cible = creature
                attack.attack(attaquant, cible)
                # Utiliser les compétences des Duplicants
                if attaquant.competences and random.random() < 0.3:
                    competence_choisie = random.choice(attaquant.competences)
                    attaquant.utiliser_competence(competence_choisie, cible)
            else:
                cible = random.choice([dup for dup in duplicants if dup.vie > 0])
                attack.attack(attaquant, cible)
            if creature.vie <= 0:
                print(f"\n{creature.nom} est vaincu!")
                for dup in duplicants:
                    dup.gagner_experience(creature.niveau * 20) # Gagner de l'XP
                break
            if any(dup.vie <= 0 for dup in duplicants):
               print("\nUn Duplicant est vaincu!")
               break
        print("\n--- Fin du Combat ---")