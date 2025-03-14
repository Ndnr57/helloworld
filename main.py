import random

def devine_le_nombre():
    print("Bienvenue dans le jeu de devinettes !")
    print("Je pense à un nombre entre 1 et 100. Essaie de deviner lequel.")

    # Le programme choisit un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    
    # Initialiser le nombre de tentatives
    tentatives = 0
    
    while True:
        # Demander au joueur de deviner un nombre
        essai = input("Entrez un nombre: ")
        
        # Vérifier que l'entrée est un nombre
        if not essai.isdigit():
            print("Ce n'est pas un nombre valide. Essaie encore.")
            continue
        
        essai = int(essai)
        tentatives += 1
        
        # Vérifier si la réponse est correcte
        if essai < nombre_secret:
            print("Trop bas ! Essaie encore.")
        elif essai > nombre_secret:
            print("Trop haut ! Essaie encore.")
        else:
            print(f"Félicitations ! Tu as trouvé le nombre secret ({nombre_secret}) en {tentatives} tentatives.")
            break

# Lancer le jeu
devine_le_nombre()
