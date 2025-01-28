import random

def lancer_pile_ou_face():
    return random.choice(['Pile', 'Face'])

def lancer_des():
    return random.randint(1, 6)

def jeu():
    choix_jeu = input("Choisissez 'pile ou face' (p) ou 'lancer de dés' (d) : ").strip().lower()

    if choix_jeu == 'p':
        choix_utilisateur = input("Choisissez 'Pile' (p) ou 'Face' (f) : ").strip().lower()
        resultat = lancer_pile_ou_face().lower()
        print(f"Le résultat est : {resultat}")
        if (choix_utilisateur == 'p' and resultat == 'pile') or (choix_utilisateur == 'f' and resultat == 'face'):
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu.")
    elif choix_jeu == 'd':
        resultat = lancer_des()
        print(f"Le résultat du lancer de dés est : {resultat}")
    else:
        print("Choix invalide. Veuillez essayer à nouveau.")

    input("Appuyez sur une touche pour fermer...")

if __name__ == "__main__":
    jeu()
