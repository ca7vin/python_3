def dmd_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERROR: Vous devez rentrer un nombre pour l'age !")
    return age_int

#demander le nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ?")

#demander l'age
age = dmd_age()

# afficher
print("Vous vous appeler " + nom + " et vous avez " + str(age) + " ans")