import turtle

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)
        
def carres(taille_depart, nb):
    for i in range(0, nb):
        taille_depart += 10
        carre(taille_depart)
        
        
t = turtle.Turtle()

carres(10, 5)

    