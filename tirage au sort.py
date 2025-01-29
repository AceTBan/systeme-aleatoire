import random  # Importation de la bibliothèque random pour générer des résultats aléatoires

# Fonction pour lancer "pile ou face"
def lancer_pile_ou_face():
    return random.choice(['Pile', 'Face'])

# Fonction pour lancer un dé
def lancer_des():
    return random.randint(1, 6)

# Fonction principale du jeu
def jeu():
    while True:  # Boucle principale pour continuer le jeu jusqu'à ce que l'utilisateur veuille quitter
        # Demande à l'utilisateur de choisir 'pile ou face' (p) ou 'lancer de dés' (d)
        choix_jeu = input("Choisissez 'pile ou face' (p) ou 'lancer de dés' (d) : ").strip().lower()

        # Fonction pour jouer une partie en fonction du choix de l'utilisateur
        def jouer_partie(choix_jeu):
            if choix_jeu == 'p':  # Si l'utilisateur choisit 'pile ou face'
                choix_utilisateur = input("Choisissez 'Pile' (p) ou 'Face' (f) : ").strip().lower()
                resultat = lancer_pile_ou_face().lower()
                print(f"Le résultat est : {resultat}")
                # Vérifie si l'utilisateur a deviné correctement
                if (choix_utilisateur == 'p' and resultat == 'pile') or (choix_utilisateur == 'f' and resultat == 'face'):
                    print("Vous avez gagné !")
                else:
                    print("Vous avez perdu.")
            elif choix_jeu == 'd':  # Si l'utilisateur choisit 'lancer de dés'
                resultat = lancer_des()
                print(f"Le résultat du lancer de dés est : {resultat}")
            else:  # Si l'utilisateur fait un choix invalide
                print("Choix invalide. Veuillez essayer à nouveau.")
        
        jouer_partie(choix_jeu)  # Appel de la fonction pour jouer une partie

        # Boucle pour demander à l'utilisateur s'il veut rejouer, changer de programme ou quitter
        while True:
            rejouer = input("Voulez-vous rejouer, changer de programme, ou quitter (r pour rejouer, c pour changer, q pour quitter) : ").strip().lower()
            if rejouer == 'r':  # Si l'utilisateur veut rejouer la même partie
                jouer_partie(choix_jeu)
            elif rejouer == 'c' or rejouer == 'q':  # Si l'utilisateur veut changer de programme ou quitter
                break
            else:  # Si l'utilisateur fait un choix invalide
                print("Choix invalide. Veuillez essayer à nouveau.")

        if rejouer == 'q':  # Si l'utilisateur veut quitter le programme
            print("Merci d'avoir joué ! Au revoir.")
            break

if __name__ == "__main__":
    jeu()  # Appel de la fonction principale du jeu
