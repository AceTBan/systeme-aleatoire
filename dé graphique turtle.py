# Importer le module turtle
import turtle
# Importer le module random
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
    for i in range(4):
        t.forward(cote)
        t.right(90)

# Définir une fonction pour dessiner un point
def point(diametre):
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
        # Un point au centre
        t.up()
        t.goto(0, -50)
        t.down()
        point(10)
    elif nombre == 2:
        # Deux points en diagonale
        t.up()
        t.goto(-25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(25, 25)
        t.down()
        point(10)
    elif nombre == 3:
        # Trois points en diagonale
        t.up()
        t.goto(-25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(0, 0)
        t.down()
        point(10)
        t.up()
        t.goto(25, 25)
        t.down()
        point(10)
    elif nombre == 4:
        # Quatre points aux coins
        t.up()
        t.goto(-25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(-25, 25)
        t.down()
        point(10)
        t.up()
        t.goto(25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(25, 25)
        t.down()
        point(10)
    elif nombre == 5:
        # Cinq points dont un au centre
        t.up()
        t.goto(-25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(-25, 25)
        t.down()
        point(10)
        t.up()
        t.goto(0, 0)
        t.down()
        point(10)
        t.up()
        t.goto(25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(25, 25)
        t.down()
        point(10)
    else:
        # Six points en deux rangées
        t.up()
        t.goto(-25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(-25, 0)
        t.down()
        point(10)
        t.up()
        t.goto(-25, 25)
        t.down()
        point(10)
        t.up()
        t.goto(25, -25)
        t.down()
        point(10)
        t.up()
        t.goto(25, 0)
        t.down()
        point(10)
        t.up()
        t.goto(25, 25)
        t.down()
        point(10)

# Créer une boucle infinie pour lancer le dé
while True:
    # Générer un nombre aléatoire entre 1 et 6
    nombre = random.randint(1, 6)
    # Dessiner le résultat du dé
    resultat(nombre)
    # Attendre une seconde
    turtle.delay(1000)
