import turtle
import random

# Créer une tortue
t = turtle.Turtle()
# Choisir la couleur et l'épaisseur du trait
t.color("black")
t.width(3)
# Cacher la tortue
t.hideturtle()
# Accélérer le dessin
t.speed(0)

# Définir une fonction pour dessiner un carré
def carre(cote):
    t.up()
    t.goto(-cote/2, cote/2)
    t.down()
    for i in range(4):
        t.forward(cote)
        t.right(90)

# Définir une fonction pour dessiner un point
def point(x, y, diametre):
    t.up()
    t.goto(x, y - diametre / 2)
    t.down()
    t.begin_fill()
    t.circle(diametre / 2)
    t.end_fill()

# Définir une fonction pour dessiner le résultat du dé
def resultat(nombre):
    # Effacer le dessin précédent
    t.clear()
    # Dessiner le contour du dé
    carre(100)
    # Choisir la couleur du point
    t.color("red")
    # Dessiner les points selon le nombre
    if nombre == 1:
        point(0, 0, 10)
    elif nombre == 2:
        point(-25, 25, 10)
        point(25, -25, 10)
    elif nombre == 3:
        point(-25, 25, 10)
        point(0, 0, 10)
        point(25, -25, 10)
    elif nombre == 4:
        point(-25, 25, 10)
        point(25, 25, 10)
        point(-25, -25, 10)
        point(25, -25, 10)
    elif nombre == 5:
        point(-25, 25, 10)
        point(25, 25, 10)
        point(0, 0, 10)
        point(-25, -25, 10)
        point(25, -25, 10)
    elif nombre == 6:
        point(-25, 25, 10)
        point(25, 25, 10)
        point(-25, 0, 10)
        point(25, 0, 10)
        point(-25, -25, 10)
        point(25, -25, 10)

# Définir une fonction pour lancer le dé
def lancer_de():
    nombre = random.randint(1, 6)
    resultat(nombre)

# Définir une fonction pour demander à l'utilisateur s'il veut relancer ou arrêter
def demander_relancer():
    answer = turtle.textinput("Lancer le dé", "Voulez-vous relancer ? (oui/non)").lower()
    if answer in ["oui", "o", "yes", "y"]:
        lancer_de()
    elif answer in ["non", "n", "no"]:
        turtle.bye()
    else:
        demander_relancer()

# Lancer le dé une première fois et demander à l'utilisateur s'il veut relancer ou arrêter
lancer_de()

# Boucle pour maintenir la fenêtre ouverte
while True:
    demander_relancer()
