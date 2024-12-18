import random

def lancer_pile_ou_face():
    resultat = random.choice(['Pile', 'Face'])
    return resultat

choix_utilisateur = input("Choisissez 'Pile' ou 'Face' : ")
resultat = lancer_pile_ou_face()
print(f"Le résultat est : {resultat}")

if choix_utilisateur.lower() == resultat.lower():
    print("Vous avez gagné !")
else:
    print("Vous avez perdu.")
