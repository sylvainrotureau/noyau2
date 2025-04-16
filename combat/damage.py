def calculate_damage(attack, defense):
    # Calcul des dégâts (à améliorer)
    degats = attack - defense
    if degats < 0:
        degats = 0
    return degats