#Projet BAC ISN

from random import *
import sys


    
def changementJoueur(gagnee):           # 
    x = randint(0,1)
    while gagnee==False:
        if x%2 == 0:
            gagnee=player1(t0,t1,t2,t3,gagnee)
        if x%2 == 1:
            gagnee=player2(t0,t1,t2,t3,gagnee)
        x = x+1
    return(gagnee)

def finDePartieGagnée():
    print("Gagné par ...")
    finDePartie()
    return()

def finDePartieEgalitee():
    print("Égalitée !")
    finDePartie()
    return()

def finDePartieDiasp():
    if gagnee==True:
        finDePartieGagnée()
        gag1=False
    return(gag1)

def finDePartie():
    print("Fin de partie !")
    gag1=False
    return(gag1)

def coupDeGagnant(t0,t1,t2,t3,gagnee):              # Détecte si les conditions pour gagner sont réunies
    if t1[0]==t1[1]==t1[2]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t2[0]==t2[1]==t2[2]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t3[0]==t3[1]==t3[2]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t1[0]==t2[0]==t3[0]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t1[1]==t2[1]==t3[1]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t1[2]==t2[2]==t3[2]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t1[0]==t2[1]==t3[2]!=" ":
        gagnee=True
        finDePartieGagnée()
    elif t3[0]==t2[1]==t1[2]!=" ":
        gagnee=True
        finDePartieGagnée()
    else:
        gagnee=False
    return(gagnee)


def player1(t0,t1,t2,t3,gagnee):                           #Pour placer le rond
    coup = int(input("Quel est votre coup?"))
    if coup == 1 and t3[0] == " ":
        t3[0] = "O"
    elif coup == 2 and t3[1] == " ":
        t3[1] = "O"
    elif coup == 3 and t3[2] == " ":
        t3[2] = "O"
    elif coup == 4 and t2[0] == " ":
        t2[0] = "O"
    elif coup == 5 and t2[1] == " ":
        t2[1] = "O"
    elif coup == 6 and t2[2] == " ":
        t2[2] = "O"
    elif coup == 7 and t1[0] == " ":
        t1[0] = "O"
    elif coup == 8 and t1[1] == " ":
        t1[1] = "O"
    elif coup == 9 and t1[2] == " ":
        t1[2] = "O"
    print (" ",t0)                                  # Afficher tableau
    print ("1",t1)
    print ("2",t2)
    print ("3",t3)
    gagnee = coupDeGagnant(t0,t1,t2,t3,gagnee)
    return(gagnee)
                    

def player2(t0,t1,t2,t3,gagnee):                           #Pour placer la Croix
    coup = int(input("Quel est votre coup?"))
    if coup == 1 and t3[0] == " ":
        t3[0] = "X"
    elif coup == 2 and t3[1] == " ":
        t3[1] = "X"
    elif coup == 3 and t3[2] == " ":
        t3[2] = "X"
    elif coup == 4 and t2[0] == " ":
        t2[0] = "X"
    elif coup == 5 and t2[1] == " ":
        t2[1] = "X"
    elif coup == 6 and t2[2] == " ":
        t2[2] = "X"
    elif coup == 7 and t1[0] == " ":
        t1[0] = "X"
    elif coup == 8 and t1[1] == " ":
        t1[1] = "X"
    elif coup == 9 and t1[2] == " ":
        t1[2] = "X"
    print (" ",t0)                                  # Afficher tableau
    print ("1",t1)
    print ("2",t2)
    print ("3",t3)
    gagnee = coupDeGagnant(t0,t1,t2,t3,gagnee)
    return(gagnee)
                    

t0 = ["A","B","C"]
t1 = [" "]*3
t2 = [" "]*3
t3 = [" "]*3

gagnee=False                                            # SI c'est vrai, arêtte le changement de joueur

while gagnee==False:
    gagnee=changementJoueur(gagnee)

    
    


