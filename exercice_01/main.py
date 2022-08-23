"""Mon premier programme Python
Formation Python sur Udemy"""


nom_character = input("Quel est ton prénom ?")
age_nextyear = 0
# boucle While
while age_nextyear == 0:
    age_character_str = input("Quel est votre age ?")
    try:
        age_nextyear = int(age_character_str)  # Conversion String -> Integer
    except ValueError:
        print("Il faut rentrer un nombre pour l'age !")
# Gestion des erreurs/exceptions, ici erreur de valeur
else:
    print("Je m'appelle " + nom_character)
    print("Je suis agé de " + age_character_str + " ans")
    print("L'an prochain, j'aurai " + str(age_nextyear + 1) + " ans")
