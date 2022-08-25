import turtle

def escalier(taille, nb):
    for i in range (0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        # taille = taille - 10
        taille -= 10
    t.forward(taille)
    
t = turtle.Turtle()

escalier(70, 5)