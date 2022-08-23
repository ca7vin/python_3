nom = ""

while nom == "":
    try:
        nom = input("Quel est votre nom ?")
    except ValueError:
        print("Entrée vide, il faut rentrer un nom !")
else:
    print ("Je m'appelle " + nom)