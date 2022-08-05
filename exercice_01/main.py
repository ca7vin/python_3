"""Mon premier programme Python
Formation Python sur Udemy"""


# On demande le nom puis l'age de la personne

# String
nom_character = input("Quel est ton prénom ?")

# Integer
age_character = input("Quel est votre age ?")

# Gestion des erreurs/exceptions, ici erreur de valeur
try:
    age_nextyear = int(age_character) + 1  # Conversion String -> Integer
except ValueError:
    print("Il faut rentrer un nombre pour l'age !")
else:
    print("Je m'appelle " + nom_character)
    print("Je suis agé de " + age_character + " ans")
    print("L'an prochain, j'aurai " + str(age_nextyear) + " ans")
