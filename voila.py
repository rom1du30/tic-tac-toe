# Tic Tac Toe par Nouguier Clément, Romain Scohy et Gaël Foppolo

import random

# Fonction d'affichage des instructions
#
# données : aucune
# résultats : les instructions qui expliquent le fonctionnement du programme
# stratégie : on appelle cette fonction uniquement au premier lancement du programme

def instructions():
    print ("Bienvenue sur le plus grand challenge de tout les temps : le Tic-Tac-Toe.\n")
    print ("Principe du jeu :")
    print ("Vous allez vous affronter sur un plateau de 3x3 cases.")
    print ("A chaque tour vous devez remplir une case de la grille, avec le symbole qui vous a été attribué en début de partie.")
    print ("La partie est gagnée quand un des joueurs a réussi à aligner 3 symboles de façon horizontale, verticale ou en diagonale.")
    print ("Deux modes possible : un contre un ou contre l'ordinateur.\n")
    print ("Vous ferez votre placement en entrant un nombre, 1 - 9. Le nombre correspond à la case du tableau comme illustré :\n")
    print ("                                     7 | 8 | 9")
    print ("                                    -----------")
    print ("                                     4 | 5 | 6")
    print ("                                    -----------")
    print ("                                     1 | 2 | 3\n")
    print ("Préparez-vous, humains. L'utltime combat va commencer.\n")
    return()

# Fonction d'affichage du plateau de jeu
#
# données : le numéro de la case si case vide, sinon X ou O
# résultats : les instructions qui expliquent le fonctionnement du programme
# stratégie : on appelle cette fonction avant de demander le placement d'un pion, pour que le joueur est un meilleure visibilité du plateau

def plateauDeJeu():
    print ("")
    print ("                                     %s | %s | %s" % (plateau[6],plateau[7],plateau[8]))
    print ("                                    -----------")
    print ("                                     %s | %s | %s" % (plateau[3],plateau[4],plateau[5]))
    print ("                                    -----------")
    print ("                                     %s | %s | %s" % (plateau[0],plateau[1],plateau[2]))
    print ("")
    return()

# Fonction de vérification "placement gagnant"
#
# données : la variable test (soit X, soit O) et le tableau "plateau"
# résultats : si coup gagant, on retourne vrai sinon on retourne faux
# stratégie : on compare pour chaque colonne (3), chaque ligne (3) et chaque diagonale (2)
#             si les trois valeurs du tableau sont égales à la variable test. Si c'est le cas on retourne vrai, sinon on retourne faux.
#             On appelle cette fonction après le placement d'un pion pour vérifier si celui-ci fait gagner la partie ou non.

def fini(test):
    if plateau[0] == test and plateau[1] == test and plateau[2] == test:
        return (True)
    if plateau[3] == test and plateau[4] == test and plateau[5] == test:
        return (True)
    if plateau[6] == test and plateau[7] == test and plateau[8] == test:
        return (True)
    if plateau[0] == test and plateau[3] == test and plateau[6] == test:
        return (True)
    if plateau[1] == test and plateau[4] == test and plateau[7] == test:
        return (True)
    if plateau[2] == test and plateau[5] == test and plateau[8] == test:
        return (True)
    if plateau[0] == test and plateau[4] == test and plateau[8] == test:
        return (True)
    if plateau[6] == test and plateau[4] == test and plateau[2] == test:
        return (True)
    return (False)

# Programme

instructions()                                                                              # Affichage des instructions
scoreJ1 = 0                                                                                 # Initialisation des compteurs du score pour les deux joueurs                                    
scoreJ2 = 0
jeu = True                                                                                  
plateau = ["1","2","3","4","5","6","7","8","9"]                                             # Création du tableau "plateau" avec les cases pré-remplies par les numéros (attention, on va de la case 0 à 8 mais contenant de 1 à 9)
joueur1 = input("Nom du joueur 1 ? ")                                                       
joueur2 = input("Nom du joueur 2 ? (tapez 'ordinateur' pour jouer contre l'ordinateur) ")

while (jeu == True):                                                                        # Tant que ce booléen est vrai le jeu continue
    plateau = ["1","2","3","4","5","6","7","8","9"]                                         # Création du tableau "plateau" avec les cases pré-remplies par les numéros car si ce n'est pas la première partie, il y aura encore le tableau de la partie précédente
    tour = 0                                                                                # Intialisation du compteur de tours
    tourJoueur = random.randint(0,1)                                                        # Intialisation de cette variable qui sert pour déterminer le tour du joueur. Si 1, c'est au joueur 1, si 0 c'est au joueur 20. Choisis au hasard 0 ou 1 pour que ce ne soit pas toujours le même qui commence la partie.
    gagner = False                                                                          # Intialisation à False
    while (tour < 9):                                                                       # Comme il n'y a que 9 cases, il ne peut y avoir que 9 tours maximum. Quand on arrive à 9, on renvoie à l'égalité.
        plateauDeJeu()
        if joueur2.lower() == "ia":
            import sys
            sys.path.append("c:\\python33")
            import ia_finale
        else :
            if tourJoueur == 1:                                                                 
                placement = input("Votre placement %s ? " % (joueur1))                          
                if plateau[(int(placement)-1)] == placement:                                    # Comparaison de la valeur rentrée par l'utilisateur et celle du numéro -1 (car on commence à 0 et non pas à 1) de la case du tableau (exemple : pour 5 rentrée on compare au contenue de la case 5-1=4). Si égal, on rentre dans la boucle sinon on redemande la placement au joueur.
                    plateau[(int(placement)-1)] = "X"                                           # Placement de la croix dans la case du tableau demandée
                    if fini("X"):                                                               # On vérifie si on a effectué un coup gagnant en appelant la fonction fini
                        gagner = True                                                           # Si c'est le cas, on affecte vrai à gagner (sans blague :p)
                        gagnant = joueur1                                                       # Le gagnant est le joueur 1
                        scoreJ1 = scoreJ1+1                                                     # Et on incrément son score de 1
                        break                                                                   # On sort de la boucle
                    tourJoueur = 0                                                              # Sinon, si ce n'est pas un coup gagant, on change le tour pour que ce soit au joueur 2
                    tour = tour+1                                                               # Et on incrémente de 1 le compteur de tour
                else:
                    print ("La case est déjà prise")                                            # Message si la case est déjà prise. On revient au if.
            else:                                                                               # Si tourJoueur est différent de 1
                if joueur2.lower() == "ordinateur":                                             # Si on a choisit de jouer contre l'ordinateur
                    placement = str(random.randrange(1,9))                                      # Le placement se fait au hasard
                    print ("Le placement de l'ordinateur est %s " % (placement))
                else:                                                                           # Sinon on joue contre le joueur 2, même code que pour le joueur 1
                    placement = input("Votre placement %s ? " % (joueur2))
                if plateau[(int(placement)-1)] == placement:
                    plateau[(int(placement)-1)] = "0"
                    if fini("0"):
                        gagner = True
                        gagnant = joueur2
                        scoreJ2 = scoreJ2+1
                        break
                    tourJoueur = 1
                    tour = tour+1
                else:
                    print ("La case est déjà prise")
    if gagner:                                                                              # Si gagner, on affiche le nom du gagant et les scores
        print ("Bravo %s, tu as gagné la partie !" % gagnant)
        print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
    else:                                                                                   # Sinon (égalitée), on affiche un pat et les scores
        print ("Damn %s, la partie avec %s est un pat..." % (joueur1,joueur2))
        print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
       
    if input("Voulez-vous jouez encore ? (O ou N) ").lower() == 'n':                        # On demande si les joueurs veulent continuer la partie
        jeu = False                                                                         # Un refus signifie une affectation False à jeu, c'est à dire la fin du programme
   
print ("Au revoir !")
