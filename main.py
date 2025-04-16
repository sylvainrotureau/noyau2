import random
from combat import combat_logic
from creatures import behavior, creature
from duplicants import skills, duplicant, inventory

def main():
    game_running = True
    duplicants_equipe = []  # Pour stocker les Duplicants

    # Création des Duplicants
    noms_duplicants = ["Alice", "Bob", "Charlie", "David"]
    classes_disponibles = ["Brute", "Eclaireur", "Ingenieur", "Chimiste"]
    for i in range(4):
        nom = noms_duplicants[i]
        classe = random.choice(classes_disponibles)
        nouveau_duplicant = duplicant.Duplicant(nom, classe, attaque=10, defense=5, vie=100, soin=2, stress=50)
        duplicants_equipe.append(nouveau_duplicant)

    # Initialiser le jeu
    print("Bienvenue dans Le Noyau!")

    # Main game loop
    while game_running:
        print("\n--- Nouveau Tour ---")
        # Handle input (exemple : une simple commande pour l'instant)
        commande = input("Entrez une commande (explorer/exit): ")

        if commande == "explorer":
            explorer(duplicants_equipe)
        elif commande == "exit":
            game_running = False
        else:
            print("Commande invalide.")

        # Update game state (exemple : combat aléatoire)
        if random.random() < 0.2:  # 20% de chance d'un combat
            print("\nUne créature sauvage apparaît!")
            creature_ennemie = creature.Creature("Araignee Geante", niveau=1, type="Insecte", attaque=12, defense=4, vie=80)
            combat_logic.handle_combat(duplicants_equipe, creature_ennemie)

        # Render output (exemple : afficher l'état des Duplicants)
        for dup in duplicants_equipe:
            print(f"\n{dup.nom} ({dup.classe}) - PV: {dup.vie}, Stress: {dup.stress}")

    # Clean up game
    print("\nMerci d'avoir joué!")

def explorer(duplicants):
    print("\nVous explorez un nouveau niveau...")
    # Placeholder pour la logique d'exploration
    print("Vous trouvez une salle sombre avec des inscriptions étranges.")

    # Exemple d'interaction (trouver un objet)
    if random.random() < 0.3:
        objet_trouve = "Ressource rare"  # À remplacer par une logique d'objet
        print(f"Vous trouvez : {objet_trouve}!")
        for dup in duplicants: # Ajouter à l'inventaire du premier Duplicant disponible
            if dup.vie > 0:
               inventory.add_item(dup, objet_trouve)
               break

if __name__ == "__main__":
    main()