# Définition de la fonction

def is_adult(age_personne):
    if age_personne >= 18:
        return True
    return False

def display_personnal_infos(nom_personne="", age_personne=0):
    # Si l'age de la personne n'est pas différent de 0, on affiche pas son age
    if nom_personne == "":
        print("Vous n'avez entré aucun nom !")
        return # Si cette condition se produit, le programme se termine
    print('La personne se nomme', nom_personne)
    print('Le prénom de', nom_personne, 'comporte', len(nom_personne), 'caractères !')
    if not age_personne == 0:
        print('La personne a', age_personne, "ans")
    if is_adult(age_personne):
        print("Il est majeur")
    else:
        print("Il est mineur")
    
# -------------------------------------------------------------------------------
print("DEBUT DU PROGRAMME")
# Appel de la fonction
age = 0
if age == 0:
    exit(0)
display_personnal_infos("Toto", age)
print()
display_personnal_infos("Popol", age)
print("FIN DU PROGRAMME")
