age = 0

def dmd_age():
    global age
    while age == 0:
        age_str = input("Quel est votre age ?")
        try:
            age = int(age_str)
        except ValueError:
            print("ERROR: Vous devez rentrer un nombre pour l'age !")

#demander le nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ?")

#demander l'age
dmd_age()

# afficher
print("Vous vous appeler " + nom + " et vous avez " + str(age) + " ans")