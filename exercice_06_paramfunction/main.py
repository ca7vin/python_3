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

def print_infos(nom_personne, age_personne):
    print("Vous vous appeler " + nom_personne + " et vous avez " + str(age_personne) + " ans")
    print("L'an prochain vous aurez " + str(age_personne+1))

#
# ------------------------------------------------------------------------
# 
#demander le nom
nom1 = dmd_nom()
nom2 = dmd_nom()

#demander l'age
age1 = dmd_age(nom1)
age2 = dmd_age(nom2)

# afficher
print_infos(nom1, age1)
print_infos(nom2, age2)