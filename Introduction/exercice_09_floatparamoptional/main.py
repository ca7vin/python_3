def dmd_nom():
    nom_response = ""
    while nom_response == "":
        nom_response = input("Quel est votre nom ?")    
    return nom_response


def dmd_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + ", quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERROR: Vous devez rentrer un nombre pour l'age !")
    return age_int

def dmd_taille(nom_personne):
    taille_float = 0
    while taille_float == 0:
        taille_str = input(nom_personne + ", quel est votre taille ?")
        try:
            taille_float = float(taille_str)
        except ValueError:
            print("ERROR: Vous devez rentrer un float pour la taille !")
    return taille_float

    
def print_infos(nom_personne, age_personne, taille_personne):
    print()
    print(f"Vous vous appeler {nom_personne} et vous avez {age_personne} ans")
    print("Vous vous appeler %s et vous avez %s ans" %(nom_personne, age_personne))
    print("L'an prochain vous aurez %s" %(age_personne+1))
    if not taille_personne == 0 :
        print("Vous mesurez " + str(taille_personne) + " M !")

    if age_personne > 60:
        print("Vous êtes senior !")
    elif age_personne == 17:
        print("Vous êtes bientôt majeur! ")
    elif 12 <= age_personne < 18 :
        print("Vous êtes adolescent !")
    elif age_personne == 18:
        print("Vous êtes tout juste majeur !")
    elif age_personne == 1 or age_personne == 2:
        print("Vous êtes bébé !")
    elif age_personne < 10:
        print("Vous êtes enfant !")
    elif age_personne > 18 :
        print("Vous êtes majeur !")
    else:
        print("Vous êtes mineur !")


#
# ------------------------------------------------------------------------
# 
# Boucle FOR

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = dmd_nom()
    age = dmd_age(nom)
    taille = dmd_taille(nom)
    print_infos(nom, age, taille)