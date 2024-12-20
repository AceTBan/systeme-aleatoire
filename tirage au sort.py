import random

def lancer_pile_ou_face():
    return random.choice(['Pile', 'Face'])

def lancer_des():
    return random.randint(1, 6)

def jeu():
    choix_jeu = input("Choisissez 'pile ou face' ou 'lancer de dés' : ").strip().lower()

    if choix_jeu == 'pile ou face':
        choix_utilisateur = input("Choisissez 'Pile' ou 'Face' : ").strip().lower()
        resultat = lancer_pile_ou_face().lower()
        print(f"Le résultat est : {resultat}")
        if choix_utilisateur == resultat:
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu.")
    elif choix_jeu == 'lancer de dés':
        resultat = lancer_des()
        print(f"Le résultat du lancer de dés est : {resultat}")
    else:
        print("Choix invalide. Veuillez essayer à nouveau.")

if __name__ == "__main__":
    jeu()
