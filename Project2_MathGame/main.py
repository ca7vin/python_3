import random


# VARIABLES
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4


# FONCTIONS
def prompt_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    
    o = random.randint(0, 3)
    operator_str = "+"
    if o == 1:
        operator_str = "+"
    elif o == 2:
        operator_str = "-"
    else:
        operator_str = "*"
         
    answer_str = input(f"Calculez {a} {operator_str} {b} = ")
    answer_int = int(answer_str)
    if o == 1:
        calcul = a + b
    elif o == 2:
        calcul = a - b
    else:
        calcul = a * b
        
    if answer_int == calcul:
        return True
    else:
        return False

# -------------------------------------------------
# PROGRAMME
score = 0
for i in range(0, NB_QUESTION):
    print(f"Question {i+1} sur {NB_QUESTION}")
    if prompt_question():
        print("Bonne réponse !")
        score += 1
    else:
        print("Mauvaise réponse")
    print()
print(f"SCORE = {score} / {NB_QUESTION}")

moyenne = int(NB_QUESTION/2)

if score == NB_QUESTION:
    print("Hello Einstein")
elif score == 0:
    print("Allez, va réviser coco !")
elif score > moyenne:
    print("Pas mal, coco !")
elif score < moyenne:
    print("Peut mieux faire, tu crois pas ?")
    