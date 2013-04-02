#Projet BAC ISN
# COntient la fonction erreur et la fonction aléatoire
from random import *



def de ():
   return() 

def player1(T):
    coup_joue=False
    t1 = T[1]
    t2 = T[2]
    t3 = T[3]
    while coup_joue == False:
                    coup = input("Svp Joueur n°1, quel est votre coup ? ")
                    if not isinstance( coup , int ):
                        print ("Rentrez un nombre svp")
                        
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
                    print (" ",t0)
                    print ("1",t1)
                    print ("2",t2)
                    print ("3",t3)
    return(T)
                    

def player2(T):
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
                    print (" ",t0)
                    print ("1",t1)
                    print ("2",t2)
                    print ("3",t3)

    return(T)


# principal

t0 = ["A","B","C"]
t1 = [" "]*3
t2 = [" "]*3
t3 = [" "]*3
T=[t0,t1,t2,t3]

print("Voici le plateau du jeu : ")
print("")
print (t0)
print (t1)
print (t2)
print (t3)
print("")
x = 0
while x < 10:
    if x%2 == 0:
        player1(T)
    if x%2 == 1:
        player2(T)
    x = x+1
