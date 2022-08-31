import random


def dmd_number(nb_min, nb_max):
    number_int = 0
    while number_int == 0:
        number_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ?")
        try:
            number_int = int(number_str)
        except:
            print("Vous devez entrer un nombre !")
        else:
            if number_int > nb_max or number_int < nb_min:
                print(f"ERREUR, le nombre doit être compris entre {nb_min} et {nb_max} !")
                number_int = 0
    return number_int

# 
# ------------------------------------------------------------------
# 

NOMBRE_MIN = 1
NOMBRE_MAX = 10
MAGIC_NUMBER = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIE = 4

win = False
for i in range(0, NOMBRE_VIE):
    vies = NOMBRE_VIE - i
    print(f"Il vous reste {vies} vies !")
    number = dmd_number(NOMBRE_MIN, NOMBRE_MAX)
    if number == MAGIC_NUMBER: 
        print("BRAVO !")
        win = True
        break
    elif number < MAGIC_NUMBER:
        print("Le nombre magique est plus grand que ça !")
    elif number > MAGIC_NUMBER:
        print("Le nombre magique est plus petit que ça !")

if win == False:
    print(f"Vous avez perdu, le nombre magique était {MAGIC_NUMBER}")