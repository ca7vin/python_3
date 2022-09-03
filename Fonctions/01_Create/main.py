# Définition de la fonction
def display_personnal_infos(nom_personne="", age_personne=0):
    # Si l'age de la personne n'est pas différent de 0, on affiche pas son age
    if nom_personne == "":
        print("Vous n'avez entré aucun nom !")
    else:
        print('La personne se nomme', nom_personne)
        print('Le prénom de', nom_personne, 'comporte', len(nom_personne), 'caractères !')
        if not age_personne == 0:
            print('La personne a', age_personne, "ans")
    
# -------------------------------------------------------------------------------

# Appel de la fonction
display_personnal_infos("Toto", 30)
display_personnal_infos("Titiche")
display_personnal_infos(age_personne=30)