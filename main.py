import random
import time
from combat import combat_logic
from creatures import behavior, creature
from duplicants import skills, duplicant, inventory
from levels import level_generation

def main():
    game_running = True
    duplicants_equipe = []
    niveau_actuel = 1
    carte_actuelle = None
    etage_max = 10 # Nombre total d'étages
    
    noms_duplicants = ["Alice", "Bob", "Charlie", "David"]
    classes_disponibles = ["Brute", "Eclaireur", "Ingenieur", "Chimiste"]
    for i in range(4):
        nom = noms_duplicants[i]
        classe = random.choice(classes_disponibles)
        nouveau_duplicant = duplicant.Duplicant(nom, classe, attaque=10, defense=5, vie=100, soin=2, stress=50)
        duplicants_equipe.append(nouveau_duplicant)

    print("Bienvenue dans Le Noyau!")
    print("\nVous vous trouvez au Portal, l'entrée d'un astéroïde mystérieux.")
    afficher_introduction()
    
    # Générer la carte du premier niveau
    carte_actuelle = level_generation.generer_carte(niveau_actuel, etage_max)

    while game_running:
        print(f"\n--- Etage {niveau_actuel} ---")
        afficher_carte(carte_actuelle)
        afficher_infos_equipe(duplicants_equipe)
        
        commande = input("Entrez une commande (ex/explorer, i/inventaire, eq/equipe, m/deplacer, q/quete, e/exit): ").lower()

        if commande in ("explorer", "ex"):
            explorer(duplicants_equipe, carte_actuelle)
        elif commande in ("inventaire", "i"):
            afficher_inventaire_equipe(duplicants_equipe)
        elif commande in ("equipe", "eq"):
            afficher_infos_equipe(duplicants_equipe)
        elif commande in ("deplacer", "m"):
            deplacer_equipe(duplicants_equipe, carte_actuelle)
        elif commande in ("quete", "q"):
            afficher_quete_principale(niveau_actuel, etage_max)
        elif commande in ("exit", "e"):
            game_running = False
        else:
            print("Commande invalide.")

        if random.random() < 0.2:
            print("\nUne créature sauvage apparaît!")
            creature_ennemie = creature.Creature("Araignee Geante", niveau=niveau_actuel, type="Insecte", attaque=12 + niveau_actuel * 2, defense=4 + niveau_actuel, vie=80 + niveau_actuel * 10)
            combat_logic.handle_combat(duplicants_equipe, creature_ennemie)
        
        # Vérifier si l'équipe peut passer à l'étage suivant
        if peut_monter_etage(duplicants_equipe, carte_actuelle):
            niveau_actuel += 1
            if niveau_actuel <= etage_max:
                print("\nL'équipe se prépare à descendre à l'étage suivant...")
                time.sleep(2)
                carte_actuelle = level_generation.generer_carte(niveau_actuel, etage_max)
            else:
                print("\nL'équipe a atteint le sommet de l'astéroïde !")
                game_running = False

        for dup in duplicants_equipe:
            dup.stress += 1  # Augmenter le stress à chaque tour
            if dup.stress > 100:
                print(f"\n{dup.nom} est en panique !")
                dup.vie -= 5  # Les Duplicants stressés perdent de la vie
            print(f"\n{dup.nom} ({dup.classe}) - PV: {dup.vie}, Stress: {dup.stress}")

    print("\nMerci d'avoir joué!")

def explorer(duplicants, carte):
    print("\nVous explorez le niveau...")
    
    # Simuler la découverte de salles et d'événements
    salle_actuelle = carte["salles"][carte["position_equipe"]]
    print(salle_actuelle["description"])
    
    # Exemple : trouver un objet
    if random.random() < 0.3:
        objet_trouve = level_generation.generer_objet(niveau_actuel)
        print(f"Vous trouvez : {objet_trouve}!")
        for dup in duplicants:
            if dup.vie > 0:
               inventory.add_item(dup, objet_trouve)
               break
    
    # Exemple : rencontrer un danger
    if random.random() < 0.15:
        danger = level_generation.generer_danger(niveau_actuel)
        print(f"Danger : {danger['description']} !")
        for dup in duplicants:
            dup.vie -= danger["degats"]
            print(f"{dup.nom} a subi {danger['degats']} points de dégâts !")

def afficher_inventaire_equipe(duplicants):
    print("\n--- Inventaire de l'équipe ---")
    for dup in duplicants:
        print(f"\n{dup.nom} ({dup.classe}):")
        if dup.inventaire:
            print(f"  {', '.join(dup.inventaire)}")
        else:
            print("  Vide")

def afficher_infos_equipe(duplicants):
    print("\n--- Infos sur l'équipe ---")
    for dup in duplicants:
        print("\n---")
        dup.afficher_infos()

def deplacer_equipe(duplicants, carte):
    print("\nOù voulez-vous déplacer l'équipe ?")
    salle_actuelle = carte["salles"][carte["position_equipe"]]
    directions_possibles = salle_actuelle["connections"]
    
    if not directions_possibles:
        print("Il n'y a pas de chemin possible depuis cette salle.")
        return
    
    for i, direction in enumerate(directions_possibles):
        print(f"{i + 1}. {direction}")
    
    choix = input("Entrez le numéro de la direction : ")
    try:
        choix_index = int(choix) - 1
        if 0 <= choix_index < len(directions_possibles):
            carte["position_equipe"] = directions_possibles[choix_index]
            print(f"L'équipe se déplace vers {directions_possibles[choix_index]}.")
        else:
            print("Choix invalide.")
    except ValueError:
        print("Entrée invalide.")

def afficher_quete_principale(niveau_actuel, etage_max):
    print("\n--- Quête Principale : L'Ascension ---")
    print("Votre objectif est d'atteindre la surface de l'astéroïde.")
    print(f"Vous êtes actuellement à l'étage {niveau_actuel} sur {etage_max}.")
    print("Trouvez des indices et des technologies pour vous aider dans votre ascension.")
    
    # Ajouter des détails de la quête au fur et à mesure de la progression
    if niveau_actuel > 3:
        print("\nVous avez trouvé des fragments d'une carte ancienne.")
    if niveau_actuel > 6:
        print("\nUn Duplicant parle d'une machine étrange qui pourrait vous aider.")

def afficher_introduction():
    print("\nVous vous réveillez au Portal, sans aucun souvenir de la façon dont vous êtes arrivés ici.")
    print("Autour de vous, trois autres Duplicants semblent aussi perdus et désorientés.")
    print("Un sentiment d'urgence vous pousse à explorer les profondeurs de l'astéroïde...")
    time.sleep(3)
    print("\nVous remarquez des inscriptions étranges sur les murs, qui semblent indiquer un chemin vers le bas.")
    print("La seule option semble être de continuer à avancer...")
    time.sleep(3)

def afficher_carte(carte):
    print("\n--- Carte du Niveau ---")
    for salle_id, salle in carte["salles"].items():
        if salle_id == carte["position_equipe"]:
            print(f"[{salle_id}] (Vous êtes ici)")
        else:
            print(f"[{salle_id}]")
    print("\nLégende :")
    for salle_id, salle in carte["salles"].items():
        print(f"[{salle_id}]: {salle['description']}")

def peut_monter_etage(duplicants, carte):
    # Logique pour vérifier si l'équipe peut monter à l'étage suivant
    # Exemple : tous les ennemis sont vaincus et l'équipe est à une salle spécifique
    salle_actuelle = carte["salles"][carte["position_equipe"]]
    if "sortie" in salle_actuelle["type"]:
        if all(dup.vie > 0 for dup in duplicants): # Tous les Duplicants doivent être en vie
           return True
    return False

if __name__ == "__main__":
    main()