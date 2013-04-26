from string import *
def Manuel() :
    print("Bonjour, voici le manuel du Tic-Tac-Toe aussi connu sous le nom de 'Morpion'")
    print("CETTE VERSION NE FONCTIONNE QU'EN 1 CONTRE 1") 
    texte=string.center("baratin", 80,"*")
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
    A=input ("Quand vous voulez commencer, appuyez sur la touche Y ")
    return(A)
        
Manuel()
reponse = accord()
if reponse == 'y':
    cls()
#{Lancer le programme}

