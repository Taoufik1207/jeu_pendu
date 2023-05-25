import random

# Liste de mots pour le jeu du pendu
mots = [] # à compléter

def choisir_mot_au_hasard():
    # Choisir un mot au hasard dans la liste
    return random.choice() # à compléter

def afficher_mot_cache(mot, lettres_trouvees):
    # Afficher le mot avec les lettres trouvées
    mot_affiche = ''
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += # à compléter
        else:
            mot_affiche += # à compléter
    return mot_affiche

def jouer_pendu():
    print("Bienvenue dans le jeu du pendu !")

    mot = choisir_mot_au_hasard()
    lettres_trouvees = []
    lettres_proposees = []
    nb_essais =  # à compléter

    while nb_essais > 0:
        print("\nMot à deviner :", afficher_mot_cache(mot, lettres_trouvees))
        print("Essais restants :", ) # à compléter
        print("Lettres déjà proposées :", ', '.join(lettres_proposees))

        lettre = input("Entrez une lettre : ").lower()

        if len(lettre) != 1:
            print("Veuillez entrer une seule lettre.")
            continue

        if lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre.")
            continue

        lettres_proposees.append() # à compléter

        if lettre in mot:
            print("Lettre trouvée !")
            lettres_trouvees.append(lettre)

            if set(mot) == set(lettres_trouvees):
                print("\nFélicitations ! Vous avez trouvé le mot :", mot)
                break
        else:
            print("Lettre incorrecte.")
            nb_essais = # à compléter

    if nb_essais == 0:
        print("\nDommage ! Vous avez épuisé tous vos essais. Le mot était :", ) # à compléter

# Appeler la fonction pour jouer au jeu du pendu
jouer_pendu()
