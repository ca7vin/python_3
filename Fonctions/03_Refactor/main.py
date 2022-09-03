# Définition de la fonction
def is_adult(age_personne):
    if age_personne >= 18:
        return True
    return False

def display_personnal_infos(nom_personne, age_personne_int, num_personne):
    if nom_personne == "":
        print("Vous n'avez entré aucun nom !")
        return
    print('La personne', num_personne ,'se nomme', nom_personne)
    print('Le prénom de', nom_personne, 'comporte', len(nom_personne), 'caractères !')
    if age_personne_int != 0:
        print('La personne a', age_personne_int, "ans")
        if is_adult(age_personne_int):
            print(f"{nom_personne} est majeur")
        else:
            print(f"{nom_personne} est mineur")

def ask_personnal_infos(num_personne):
    nom_personne = input(f"Personne {num_personne}, quel est votre prénom ?")
    age_personne = input(f"{nom_personne}, quel est votre âge ?")
    age_personne_int = int(age_personne)
    display_personnal_infos(nom_personne, age_personne_int, num_personne)
    
# -------------------------------------------------------------------------------

# Appel de la fonction
NB_PERSONNES = 2

for i in range(0, NB_PERSONNES):
    ask_personnal_infos(i+1)