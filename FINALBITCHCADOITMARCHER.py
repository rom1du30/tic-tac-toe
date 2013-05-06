#!/usr/bin/env python3
# LULZ Gé tou trièèè léé def com' ci on lencèè le gramepro de labitchetoitmémetulesé
#!/usr/bin/env python3
# PROJET FINAL 

from random import *

### Fonction Manuel ###
def Manuel() :
    print("Bonjour, voici le manuel du Tic-Tac-Toe aussi connu sous le nom de 'Morpion'")
    print("CETTE VERSION NE FONCTIONNE QU'EN 1 CONTRE 1")
    print("Principe \n Du \n Jeu ")
    print("Vous allez vous affronter sur un plateau de 3x3 cases.")
    print("A chaque tour vous devez remplir une case de la grille, avec le symbole qui vous a été attribué en début de partie.")
    print("La partie est gagnée quand des joueurs a réussi à aligner 3 symboles de façon horizontale, verticale ou en diagonale.")
    print("Bon Jeux =)")
    return()

def cls():
    print(" \n " * 100)
    return()
def accord():
    A=input ("Quand vous voulez commencer, appuyez sur la touche Y : ")
    return(A)

### Choix un joueur ###

def changementJoueur(gagnee): #
    x = randint(0,1)
    while gagnee==False:
        if x%2 == 0:
            gagnee=player1(T)
        if x%2 == 1:
            gagnee=player2(T)
        x = x+1
    return(gagnee)

##### Placement du signe ####

def player1(T): #Pour placer le rond   #(t0,t1,t2,t3,gagnee)
    gagnee=False
    coup_joue=False
    t1 = T[1]
    t2 = T[2]
    t3 = T[3]
    while coup_joue == False:
        coup = int(input("Svp Joueur n°1, quel est votre coup ? "))
    
        if coup == 1 and t3[0] == " ":
                t3[0] = "O"
                coup_joue = True
        elif coup == 2 and t3[1] == " ":
            t3[1] = "O"
            coup_joue = True
        elif coup == 3 and t3[2] == " ":
            t3[2] = "O"
            coup_joue = True
        elif coup == 4 and t2[0] == " ":
            t2[0] = "O"
            coup_joue = True
        elif coup == 5 and t2[1] == " ":
            t2[1] = "O"
            coup_joue = True
        elif coup == 6 and t2[2] == " ":
            t2[2] = "O"
            coup_joue = True
        elif coup == 7 and t1[0] == " ":
            t1[0] = "O"
            coup_joue = True
        elif coup == 8 and t1[1] == " ":
            t1[1] = "O"
            coup_joue = True
        elif coup == 9 and t1[2] == " ":
            t1[2] = "O"
            coup_joue = True
        else :
            print ("Pourquoi placer un pion sur une place déjà prise ? Recommencez s'il vous plaît. ")
    print (" ",t0) # Afficher tableau
    print ("1",t1)
    print ("2",t2)
    print ("3",t3)
    gagnee = coupDeGagnant(T,gagnee)
    return(gagnee)

def player2(T): #Pour placer la Croix
    gagnee = False
    coup_joue=False
    t1 = T[1]
    t2 = T[2]
    t3 = T[3]
    while coup_joue == False:
        coup = int(input("Svp Joueur n°2, quel est votre coup ? "))
        if coup == 1 and t3[0] == " ":
            t3[0] = "X"
            coup_joue = True
        elif coup == 2 and t3[1] == " ":
            t3[1] = "X"
            coup_joue = True
        elif coup == 3 and t3[2] == " ":
            t3[2] = "X"
            coup_joue = True
        elif coup == 4 and t2[0] == " ":
            t2[0] = "X"
            coup_joue = True
        elif coup == 5 and t2[1] == " ":
            t2[1] = "X"
            coup_joue = True
        elif coup == 6 and t2[2] == " ":
            t2[2] = "X"
            coup_joue = True
        elif coup == 7 and t1[0] == " ":
            t1[0] = "X"
            coup_joue = True
        elif coup == 8 and t1[1] == " ":
            t1[1] = "X"
            coup_joue = True
        elif coup == 9 and t1[2] == " ":
            t1[2] = "X"
            coup_joue = True
        else :
            print ("Pourquoi placer un pion sur une place déjà prise ? Recommencez s'il vous plaît. ")
    print (" ",t0) # Afficher tableau
    print ("1",t1)
    print ("2",t2)
    print ("3",t3)
    gagnee = coupDeGagnant(T,gagnee)
    return(gagnee)

### Verification du coup joué ###

def coupDeGagnant(T,gagnee): # Détecte si les conditions pour gagner sont réunies
    t1 = T[1]
    t2 = T[2]
    t3 = T[3]
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

### Arrêt de la partie ###

def finDePartieGagnée():
    print("Gagné par ...")
    finDePartie()
    return()

def finDePartie():
    print("Fin de partie !")
    gag1=False
    return(gag1)

####### CEUX QUI NE SERVENT PAS A GRAND CHOSE MAIS QU'ON GARDE QUAND MÊME #######
def finDePartieEgalitee():
    print("Égalitée !")
    finDePartie()
    return()

def finDePartieDiasp():
    if gagnee==True:
        finDePartieGagnée()
        gag1=False
    return(gag1)

   ##########################################
  ############################################
################## PROGRAMMME ##################
  ############################################
   ##########################################


### Création du tableau ###
t0 = ["A","B","C"]
t1 = [" "]*3
t2 = [" "]*3
t3 = [" "]*3

T=[t0,t1,t2,t3]

### Affichage du Manuel ###

Manuel()
reponse = accord()
if reponse == y :
    cls()

### Affichage du tableau ###

print("Voici le plateau du jeu : ")
print("")
print (t0)
print (t1)
print (t2)
print (t3)
print("")

### Programme en lui-même ###

gagnee=False

while gagnee==False:
    gagnee=changementJoueur(gagnee)
