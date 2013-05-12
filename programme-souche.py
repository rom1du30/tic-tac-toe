#Tic Tac Toe
import random


def instructions():
    print ("Bienvenue sur le plus grand challenge de tout les temps : le Tic-Tac-Toe.\n")
    print ("Principe du jeu :")
    print ("Vous allez vous affronter sur un plateau de 3x3 cases.")
    print ("A chaque tour vous devez remplir une case de la grille, avec le symbole qui vous a été attribué en début de partie.")
    print ("La partie est gagnée quand un des joueurs a réussi à aligner 3 symboles de façon horizontale, verticale ou en diagonale.")
    print ("Deux modes possible : un contre un ou contre l'ordinateur.\n")
    print ("Vous ferez votre placement en entrant un nombre, 1 - 9. Le nombre correspond à la case du tableau comme illustré :\n")
    print ("Il est conseillé d'utiliser le Pavé Numérique !")
    print ("                                     7 | 8 | 9")
    print ("                                    -----------")
    print ("                                     4 | 5 | 6")
    print ("                                    -----------")
    print ("                                     1 | 2 | 3\n")
    print ("Préparez-vous, humains. L'utltime combat va commencer.\n")
    return()

def drawboard():
    print
    print ("-------------")
    print ("| %s | %s | %s |" % (plateau[6],plateau[7],plateau[8]))
    print ("-------------")
    print ("| %s | %s | %s |" % (plateau[3],plateau[4],plateau[5]))
    print ("-------------")
    print ("| %s | %s | %s |" % (plateau[0],plateau[1],plateau[2]))
    print ("-------------")
    print
    return()
   

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


    

#Programme
scoreJ1 = 0
scoreJ2 = 0
jeu = True
instructions()
plateau = ["1","2","3","4","5","6","7","8","9"]
joueur1 = input("Nom du joueur 1 ? ")
joueur2 = input("Nom du joueur 2 ? (tapez 'IA' pour jouer contre l'ordinateur) ")

while (jeu == True):
    plateau = ["1","2","3","4","5","6","7","8","9"]
    tour = 0
    tourIA = 0
    tourJoueur = 1
    gagner = False
    placement = None
    while (tour < 9):
        drawboard()
        if joueur2.lower() == "ia":
            import sys
            sys.path.append("c:\\python33")
            import IA_BAC
        
        if tourJoueur == 1:
            placement = input("Votre placement %s ? " % (joueur1))
            if plateau[(int(placement)-1)] == placement:
                plateau[(int(placement)-1)] = "O"
                if fini("O"):
                    gagner = True
                    gagnant = joueur1
                    scoreJ1 = scoreJ1+1
                    break
                tourJoueur = 0
                tour = tour+1
                drawboard()
            else:
                print ("Le placement est invalide ou la case est déjà prise")
        if joueur2.lower() != "ia":
                placement = input("Votre placement %s ? " % (joueur2))
                if plateau[(int(placement)-1)] == placement:
                    plateau[(int(placement)-1)] = "X"
                    if fini("X"):
                        gagner = True
                        gagnant = joueur2
                        scoreJ2 = scoreJ2+1
                        break
                    tourJoueur = 1
                    tour = tour+1
                else:
                    print ("Le placement est invalide ou la case est déjà prise")
    if gagner:
        print ("Bravo %s, tu as gagné la partie !" % gagnant)
        print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
    else:
        print ("La partie se termine sur un match nul !" % (joueur1,joueur2))
        print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
       
    if  input("Voulez-vous jouez encore ? (O ou N) ").lower() == 'n':
        jeu = False
   
print ("Au revoir !")


