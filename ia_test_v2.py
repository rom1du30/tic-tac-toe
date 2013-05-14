# IL FAUT VERFIER SI CA MARCHE, CHEZ MOI J'AI UNE ERREUR SYNTAXE DE MERDE, DONC FUCK.
# LE PROGRAMME NE S'ARRETTE PAS? J'AI JUSTE OUBLIE DE PLACER LE JEU = FALSE.
# VOILA

# les Definitions
def IA1(T):
    plateau[0] = "X"
    return ()

def IA2(T):
    plateau[1] = "X"
    return ()

def IA3(T):
    plateau[2] = "X"
    return ()

def IA4(T):
    plateau[3] = "X"
    return ()

def IA5(T):
    plateau[4] = "X"
    return ()

def IA6(T):
    plateau[5] = "X"
    return ()

def IA7(T):
    plateau[6] = "X"
    return ()

def IA8(T):
    plateau[7] = "X"
    return ()

def IA9(T):
    plateau[8] = "X"
    return ()



def Win(T):
    if plateau[6]=="X" and plateau[7]=="X":
        if plateau[8]== " ":
            plateau[8]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]==plateau[8]=="X":
        if plateau[7] == " ":
            plateau[7]= "X"
            print ("Victoire de l'IA!")
    if plateau[7]=="X" and plateau[8]=="X":
        if plateau[8] == " ":
            plateau[6]= "X"
            print ("Victoire de l'IA!")
    if plateau[3]=="X" and plateau[4]=="X":
        if plateau[5] == " ":
            plateau[5]= "X"
            print ("Victoire de l'IA!")
    if plateau[3]=="X" and plateau[5]=="X":
        if plateau[4] == " ":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[5]=="X":
        if plateau[3] == " ":
            plateau[3]= "X"
            print ("Victoire de l'IA!")
    if plateau[0]=="X" and plateau[1]=="X":
        if plateau[2] == " ":
            plateau[2]= "X"
            print ("Victoire de l'IA!")
    if plateau[0]=="X" and plateau[2]=="X":
        if plateau[1] == " ":
            plateau[1]= "X"
            print ("Victoire de l'IA!")
    if plateau[1]=="X" and plateau[2]=="X":
        if plateau[0] == " ":
            plateau[0]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[4]=="X":
        if plateau[2] == " ":
            plateau[2]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[2]=="X":
        if plateau[4] == " ":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[2]=="X":
        if plateau[6] == " ":
            plateau[6]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[4]=="X":
        if plateau[0] == " ":
            plateau[0]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[0]=="X":
        if plateau[4] == " ":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[0]=="X":
        if plateau[8] == " ":
            plateau[8]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[3]=="X":
        if plateau[0] == " ":
            plateau[0]= "X"
            print ("Victoire de l'IA!")
    if plateau[6]=="X" and plateau[0]=="X":
        if plateau[3] == " ":
            plateau[3]= "X"
            print ("Victoire de l'IA!")
    if plateau[3]=="X" and plateau[0]=="X":
        if plateau[6] == " ":
            plateau[6]= "X"
            print ("Victoire de l'IA!")
    if plateau[7]=="X" and plateau[4]=="X":
        if plateau[1] == " ":
            plateau[1]= "X"
            print ("Victoire de l'IA!")
    if plateau[7]=="X" and plateau[1]=="X":
        if plateau[4] == " ":
            plateau[4]= "X"
            print ("Victoire de l'IA!")
    if plateau[4]=="X" and plateau[1]=="X":
        if plateau[7] == " ":
            plateau[7]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[5]=="X":
        if plateau[2] == " ":
            plateau[2]= "X"
            print ("Victoire de l'IA!")
    if plateau[8]=="X" and plateau[2]=="X":
        if plateau[5] == " ":
            plateau[5]= "X"
            print ("Victoire de l'IA!")
    if plateau[5]=="X" and plateau[2]=="X":
        if plateau[8] == " ":
            plateau[8]= "X"
            print ("Victoire de l'IA!")




   ##########################################
  ############################################
################## PROGRAMMME ##################
  ############################################
   ##########################################

while (jeu == True):
    plateau = ["1","2","3","4","5","6","7","8","9"]
    tour = 0 # Compteur de tours
    tourJoueur = random.randint(0,1)
    gagner = False
    while (tour < 9): # Si le compteur arrive à 9, on renvoit au cas d'égalité
        drawboard() # On affiche à chaque tour le plateau
        coup = int(input("Votre placement %s ? " % (joueur1))
        # On extraie d'ici
        if coup == 1 and plateau[0] == " "
            plateau[0] = "O"
            Win(T)
            if tour == 0:
                IA9(T)
                tour = 719
            if tour == 75382:
                IA9(T)
                tour = 7538219
            if coup == 75364:
                IA9(T)
                tour = 7536419
            if tour == 753:
                IA9(T)
                tour = 75319
            turn = turn+1
        if coup == 2 and plateau[1] == " ":
            plateau[1] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 725
            if tour == 753:
                IA8
                tour = 75328
            if tour == 7534691:
                IA8(T)
                print ("Damn %s, la partie avec %s se termine par égalité !" % (joueur1,joueur2))
            turn = turn+1
        if coup == 3 and plateau[2] == " ":
            plateau[2] = "O"
            Win(T)
            if tour == 0:
                IA9(T)
                tour = 739
            if tour == 785:
                IA1(T)
                tour = 7851
            if tour == 765:
                IA9(T)
                tour = 7659
            if tour == 725:
                IA1(T)
                tour = 7251
            if tour == 745:
                IA9(T)
                tour = 7459
            turn = turn+1
        if coup == 4 and plateau[3] == " ":
            plateau[3] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 745
            if tour == 791:
                IA3(T)
                tour = 7914
            if tour == 7532891:
                IA6(T)
                print ("Damn %s, la partie avec %s se termine par égalité !" % (joueur1,joueur2))
            if tour == 753:
                IA6(T)
                tour = 75346
            turn = turn+1
        if coup == 5 and plateau[4] == " ":
            plateau[4] = "O"
            Win(T)
            if tour == 0:
                IA3(T)
                tour = 753
            turn = turn+1
        if coup == 6 and plateau[5] == " ":
            plateau[5] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 765
            if tour == 7538219:
                IA4(T)
                print ("Damn %s, la partie avec %s se termine par égalité !" % (joueur1,joueur2))
            if tour == 753:
                IA4(T)
                tour = 75364
            turn = turn+1
        if coup == 7 and plateau[6] == " ":
            plateau[6] = "O"
        if coup == 8 and plateau[7] == " ":
            plateau[7] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 785
            if tour == 739:
                IA1(T)
                tour = 7391
            if tour == 719:
                IA3(T)
                tour = 7193
            if tour == 753:
                IA2(T)
                tour = 75382
            if tour == 7536419:
                IA2(T)
                print ("Damn %s, la partie avec %s se termine par égalité !" % (joueur1,joueur2))
            turn = turn+1
        if coup == 9 and plateau[8] == " ":
            plateau[8] = "O"
            Win(T)
            if tour == 0:
                IA1(T)
                tour = 791
            if tour == 753:
                IA1(T)
                tour = 75391
            if tour == 75328:
                IA1(T)
                tour = 7532891
            if tour == 75346:
                IA1(T)
                tour = 7534691
            turn = turn+1
        # A ici
        
        
        
        
        #if tourJoueur == 1: # C'est au joueur 1 de jouer
        # placement = input("Votre placement %s ? " % (joueur1)) # On demande quel placement il veut effectuer
        # if plateau[(int(placement)-1)] == placement: # PAS COMPRIS
        # plateau[(int(placement)-1)] = "X" # La croix est placée
        #
        # else: # Si le placement est invalide, le joueur 1 recommence
        # print ("Le placement est invalide ou la case est déjà prise")
        #else: # C'est au Joueur 2 de jouer.
        # if joueur2.lower() == "ordinateur": # Si on a choisit de jouer contre l'IA
        # placement = str(random.randrange(1,9)) # Alors l'IA place au hasard un coup
        # print ("Le placement de l'ordinateur est %s " % (placement))
            #else: # Si on a choisit de jouer contre qqun d'autre
            # placement = input("Votre placement %s ? " % (joueur2)) # On demande quel placement il veut effectuer
            #if plateau[(int(placement)-1)] == placement: # PAS COMPRIS
            # plateau[(int(placement)-1)] = "0" # Le Rond est placée
            # if fini("0"): # On vérifié si on a effectué un coup gagnant en appelant la def Fini.
            # gagner = True # Si le coup est gagnant, alors on affecte vrai à "gagner"
            # gagnant = joueur2 # On informe que le vainqueur est le joueur 1
            # scoreJ2 = scoreJ2+1 # On augmente de 1 son score
            # break
            # tourJoueur = 1 # Sinon on passe au Joueur 1
            # tour = tour+1
            #else:
            # print ("le placement est invalide ou la case est déjà prise")
    #if gagner: # il manque pas un True ? # Quand la partie est gagnée, on affiche le gagnant, le score
    # print ("Bravo %s, tu as gagné la partie !" % gagnant)
    # print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
    #else:
    # print ("Damn %s, la partie avec %s se termine par égalité !" % (joueur1,joueur2)) # Sinon, il y a égalité, les scores ne changent pas
    # print ("Le score est de ",scoreJ1," pour ",joueur1,"et de",scoreJ2," pour",joueur2,)
    #
    if input("Voulez-vous jouez encore ? (O ou N) ").lower() == 'n': # Permet de rejouer ou non
        jeu = False
   
