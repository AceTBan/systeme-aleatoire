import turtle
import random

# Créer une tortue pour dessiner
t = turtle.Turtle()
# Choisir la couleur et l'épaisseur du trait de la tortue
t.color("black")
t.width(3)
# Cacher la tortue pour que le curseur ne soit pas visible pendant le dessin
t.hideturtle()
# Accélérer le dessin pour qu'il soit plus rapide
t.speed(0)

# Définir une fonction pour dessiner un carré avec un côté de longueur 'cote'
def carre(cote):
    t.up()  # Lever le stylo pour ne pas dessiner en se déplaçant
    t.goto(-cote/2, cote/2)  # Se déplacer au coin supérieur gauche du carré
    t.down()  # Abaisser le stylo pour commencer à dessiner
    for i in range(4):  # Répéter 4 fois pour dessiner les 4 côtés du carré
        t.forward(cote)  # Dessiner un côté du carré
        t.right(90)  # Tourner à droite de 90 degrés

# Définir une fonction pour dessiner un point de diamètre 'diametre' à la position (x, y)
def point(x, y, diametre):
    t.up()  # Lever le stylo pour se déplacer sans dessiner
    t.goto(x, y - diametre / 2)  # Se déplacer au centre du cercle
    t.down()  # Abaisser le stylo pour commencer à dessiner
    t.begin_fill()  # Commencer à remplir le cercle
    t.circle(diametre / 2)  # Dessiner un cercle
    t.end_fill()  # Terminer le remplissage du cercle

# Définir une fonction pour dessiner le résultat du dé en fonction du nombre obtenu
def resultat(nombre):
    t.clear()  # Effacer le dessin précédent
    carre(100)  # Dessiner le contour du dé avec un côté de 100 unités
    t.color("red")  # Choisir la couleur rouge pour les points
    # Dessiner les points selon le nombre obtenu
    if nombre == 1:
        point(0, 0, 10)  # Un point au centre
    elif nombre == 2:
        point(-25, 25, 10)  # Deux points en diagonale
        point(25, -25, 10)
    elif nombre == 3:
        point(-25, 25, 10)  # Trois points en diagonale
        point(0, 0, 10)
        point(25, -25, 10)
    elif nombre == 4:
        point(-25, 25, 10)  # Quatre points aux coins
        point(25, 25, 10)
        point(-25, -25, 10)
        point(25, -25, 10)
    elif nombre == 5:
        point(-25, 25, 10)  # Cinq points (quatre aux coins et un au centre)
        point(25, 25, 10)
        point(0, 0, 10)
        point(-25, -25, 10)
        point(25, -25, 10)
    elif nombre == 6:
        point(-25, 25, 10)  # Six points en deux rangées
        point(25, 25, 10)
        point(-25, 0, 10)
        point(25, 0, 10)
        point(-25, -25, 10)
        point(25, -25, 10)

# Définir une fonction pour lancer le dé et obtenir un nombre aléatoire entre 1 et 6
def lancer_de():
    nombre = random.randint(1, 6)  # Générer un nombre aléatoire entre 1 et 6
    resultat(nombre)  # Dessiner le résultat du dé

# Définir une fonction pour demander à l'utilisateur s'il veut relancer ou arrêter
def demander_relancer():
    # Demander à l'utilisateur s'il veut relancer ou arrêter
    answer = turtle.textinput("Lancer le dé", "Appuyez sur Entrée pour relancer ou tapez 'n' pour arrêter : ").lower()
    if answer == "" or answer in ["oui", "o", "yes", "y"]:  # Si l'utilisateur appuie sur Entrée ou dit oui
        lancer_de()  # Lancer le dé à nouveau
    elif answer in ["non", "n", "no"]:  # Si l'utilisateur dit non
        turtle.bye()  # Fermer la fenêtre Turtle
    else:
        demander_relancer()  # Redemander à l'utilisateur s'il veut relancer ou arrêter

# Lancer le dé une première fois et demander à l'utilisateur s'il veut relancer ou arrêter
lancer_de()

# Boucle pour maintenir la fenêtre ouverte
while True:
    demander_relancer()
