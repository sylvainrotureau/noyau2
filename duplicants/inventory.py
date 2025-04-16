def add_item(duplicant, item):
    duplicant.inventaire.append(item)
    print(f"{duplicant.nom} a ajouté {item} à son inventaire.")

def use_item(duplicant, item):
   if item in duplicant.inventaire:
      print(f"{duplicant.nom} utilise {item}")
      duplicant.inventaire.remove(item)
   else:
      print(f"{duplicant.nom} n'a pas cet objet")