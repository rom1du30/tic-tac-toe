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

def IA1(plateau):
    plateau[0] = "X"
    


def IA2(plateau):
    plateau[1] = "X"
    


def IA3(plateau):
    plateau[2] = "X"
    


def IA4(plateau):
    plateau[3] = "X"
    

def IA5(plateau):
    plateau[4] = "X"
    


def IA6(plateau):
    plateau[5] = "X"
    


def IA7(plateau):
    plateau[6] = "X"
    

def IA8(plateau):
    plateau[7] = "X"
    

def IA9(plateau):
    plateau[8] = "X"
    
        
def Win(plateau):
    if plateau[6]=="X" and plateau[7]=="X":
        if plateau[8] == "9":
            plateau[8] = "X"
            print ("Victoire de l'IA!") 
    if plateau[6]==plateau[8]=="X":
        if plateau[7] == "8":
            plateau[7]= "X"
            print ("Victoire de l'IA!")
    if plateau[7]=="X" and plateau[8]=="X":
        if plateau[8] == "9":
            plateau[6]= "X"
            print ("Victoire de l'IA!")
    if plateau[3]=="X" and plateau[4]=="X":
        if plateau[5] == "6":
            plateau[5]= "X"
            print ("Victoire de l'IA!")
    if plateau[3]=="X" and plateau[5]=="X":
        if plateau[4] == "5":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[5]=="X":
        if plateau[3] == "4":
            plateau[3]= "X"
            print ("Victoire de l'IA!")
    if plateau[0]=="X" and plateau[1]=="X":
        if plateau[2] == "3":
            plateau[2]= "X"
            print ("Victoire de l'IA!")
    if plateau[0]=="X" and plateau[2]=="X":
        if plateau[1] == "2":
            plateau[1]= "X"
            print ("Victoire de l'IA!")
    if plateau[1]=="X" and plateau[2]=="X":
        if plateau[0] == "1":
            plateau[0]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[4]=="X":
        if plateau[2] == "3":
            plateau[2]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[2]=="X":
        if plateau[4] == "5":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[2]=="X":
        if plateau[6] == "7":
            plateau[6]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[4]=="X":
        if plateau[0] == "1":
            plateau[0]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[0]=="X":
        if plateau[4] == "5":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[0]=="X":
        if plateau[8] == "9":
            plateau[8]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[3]=="X":
        if plateau[0] == "1":
            plateau[0]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[0]=="X":
        if plateau[3] == "4":
            plateau[3]= "X"
            print ("Victoire de l'IA!")
    if plateau[3]=="X" and plateau[0]=="X":
        if plateau[6] == "7":
            plateau[6]= "X"
            print ("Victoire de l'IA!")
    if plateau[7]=="X" and plateau[4]=="X":
        if plateau[1] == "2":
            plateau[1]= "X"
            print ("Victoire de l'IA!")
    if plateau[7]=="X" and plateau[1]=="X":
        if plateau[4] == "5":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[1]=="X":
        if plateau[7] == "8":
            plateau[7]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[5]=="X":
        if plateau[2] == "3":
            plateau[2]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[2]=="X":
        if plateau[5] == "6":
            plateau[5]= "X"
            print ("Victoire de l'IA!")
    if plateau[5]=="X" and plateau[2]=="X":
        if plateau[8] == "9":
            plateau[8]= "X"
            print ("Victoire de l'IA!")


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
            else:
                print ("Le placement est invalide ou la case est déjà prise")
        else:
            if joueur2.lower() == "ia":
                ##### placement = str(random.randrange(1,9)) #####
                if placement is None :
                    IA7(plateau)
                    tourIA == 0
                    if fini("X"):
                        gagner = True
                        gagnant = joueur2
                        scoreJ2 = scoreJ2+1
                        break
                    tourJoueur = 1
                    tour = tour+1
                if placement == 1 :
                    Win(plateau)
                    if tourIA == 0:
                        IA9(plateau)
                        tourIA = 719
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1                        
                    if tourIA == 75382:
                        IA9(plateau)
                        tourIA = 7538219
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 75364:
                        IA9(plateau)
                        tourIA = 7536419
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 753:
                        IA9(plateau)
                        tourIA = 75319
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                     
                if placement == 2 :
                    Win(plateau)
                    if tourIA == 0:
                        IA5(plateau)
                        tourIA = 725
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 753:
                        IA8(plateau)
                        tourIA = 75328
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1                        
                    if tourIA == 7534691:
                        IA8(plateau)
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                if placement == 3 :
                    Win(plateau)
                    if tourIA == 0:
                        IA9(plateau)
                        tourIA = 739
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 785:
                        IA1(plateau)
                        tour = 7851
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 765:
                        IA9(plateau)
                        tourIA = 7659
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 725:
                        IA1(plateau)
                        tourIA = 7251
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 745:
                        IA9(plateau)
                        tourIA = 7459
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1 
                if placement == 4 :
                    Win(plateau)
                    if tourIA == 0:
                        IA5(plateau)
                        tourIA = 745
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 791:
                        IA3(plateau)
                        tourIA = 7914
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 7532891:
                        IA6(plateau)
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 753:
                        IA6(plateau)
                        tourIA = 75346
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                if placement == 5 :
                    Win(plateau)
                    if tourIA == 0:
                        IA3(plateau)
                        tourIA = 753
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1 
                if placement == 6 :
                    Win(plateau)
                    if tourIA == 0:
                        IA5(plateau)
                        tourIA = 765
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 7538219:
                        IA4(plateau)
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 753:
                        IA4(plateau)
                        tourIA = 75364
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                if placement == 7 :
                    if fini("X"):
                        gagner = True
                        gagnant = joueur2
                        scoreJ2 = scoreJ2+1
                        break
                    tourJoueur = 1
                    tour = tour+1
                if placement == 8 and plateau[7] == "8":
                    plateau[7] = "X"
                    Win(plateau)
                    if tourIA == 0:
                        IA5(plateau)
                        tourIA = 785
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 739:
                        IA1(plateau)
                        tourIA = 7391
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 719:
                        IA3(plateau)
                        tourIA = 7193
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 753:
                        IA2(plateau)
                        tourIA = 75382
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 7536419:
                        IA2(plateau)
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                if placement == 9 :
                    Win(plateau)
                    if tourIA == 0:
                        IA1(plateau)
                        tourIA = 791
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 753:
                        IA1(plateau)
                        tourIA = 75391
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 75328:
                        IA1(plateau)
                        tourIA = 7532891
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    if tourIA == 75346:
                        IA1(plateau)
                        tourIA = 7534691
                        if fini("X"):
                            gagner = True
                            gagnant = joueur2
                            scoreJ2 = scoreJ2+1
                            break
                        tourJoueur = 1
                        tour = tour+1
                    else:
                        print ("Le placement est invalide ou la case est déjà prise")
            else:
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
        print ("Damn %s, la partie avec %s est un pat..." % (joueur1,joueur2))
        print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
       
    if  input("Voulez-vous jouez encore ? (O ou N) ").lower() == 'n':
        jeu = False
   
print ("Au revoir !")
