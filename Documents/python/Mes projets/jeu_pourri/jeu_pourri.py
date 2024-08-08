### Modules

import random

### Situation de départ :

pt_vie_j = 50
pt_vie_en = 50
potions_j = 3
passe_tour = False
choix_joueur = ""


print("-" * 50)
print(f"Vous avez {pt_vie_j} points de vie. votre adversaire à {pt_vie_en}. Vous avez {potions_j} potions.")
print("-" * 50)

## Je définis le jeu

while True:

    if passe_tour == True:
        print("Vous passez votre tour")
        passe_tour = False
    
    ## Le joueur choisi une potion ou l'attaque
     
    else:
        
        choix_joueur = ""
        while choix_joueur not in ["1", "2"]:
            choix_joueur = input("Souhaitez-vous attaquer ou prendre une potion ? \n 1 : Attaquer. \n 2 : Potion. \n")
            
        if choix_joueur == "1":
            attaque_j = random.randint(5,10)
            pt_vie_en -= attaque_j
            print(f"Vous avez infligé {attaque_j} points à l'ennemi.")
            
        if choix_joueur == "2" and potions_j > 0:
            pt_vie_recup = random.randint(15,50)
            pt_vie_j += pt_vie_recup
            potions_j -= 1
            print(f"Vous avez recupéré {pt_vie_recup} points de vie.")
            print(f"Il vous reste {potions_j} potions.")
            passe_tour = True  
        
        if choix_joueur == "2" and potions_j == 0:
            print("Vous n'avez plus de potions")
            continue

    if pt_vie_en <= 0:
        print("Vous avez gagné")
        break

    attaque_en = random.randint(5,15)
    pt_vie_j -= attaque_en
    print(f"Votre ennemeni à infligé {attaque_en} points.")

    if pt_vie_j <= 0:
        print("Vous avez perdu")
        break

    print(f"Il vous reste {pt_vie_j} points de vie. \nIl reste {pt_vie_en} points de vie à votre adversaire. \nIl vous reste {potions_j} potions.")
    print("-" * 50)

### Fin du jeu :

