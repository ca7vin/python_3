# FUNCTIONS

def ask_question(question, answ1, answ2, answ3, answ4, right_answer):
    print("QUESTION :")
    print(question)
    print(f"A :{answ1}")
    print(f"B :{answ2}")
    print(f"C :{answ3}")
    print(f"D :{answ4}")
    print()
    user_answ = input("Votre réponse : ")
    if user_answ == right_answer:
        print("BONNE REPONSE !")
    else:
        print("MAUVAISE REPONSE !")


# ------------------------------
# PROGRAM

q1 = "Quelle est la couleur du cheval blanc de Napoléon ?"
q2 = "Qui est le plus grand ?"
q3 = "Calculez 6 x 7"
q4 = "Que mangent les singes ?"

ask_question(q1, "blanc", "vert", "jaune", "rouge", "A")
print()
ask_question(q2, "10", "100", "100", "1", "C")
print()
ask_question(q3, "12", "37", "42", "19", "C")
print()
ask_question(q4, "compote", "poires", "raisins", "bananes", "D")
print()