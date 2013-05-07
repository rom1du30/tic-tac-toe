
t0 = ["A","B","C"]
t1 = [" "]*3
t2 = [" "]*3
t3 = [" "]*3

T = (t0,t1,t2,t3)

def changementJoueur(T):
            IA7(T)
            print (" ",t0)
            print ("1",t1)
            print ("2",t2)
            print ("3",t3)
            player1(T)
                
def player1(T):
    turn = 0
    tour = 0
    while turn<10:
        coup = int(input("Quel est votre coup?"))
        if coup == 1 and t3[0] == " ":
            t3[0] = "O"
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
        if coup == 2 and t3[1] == " ":
            t3[1] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 725
            if tour == 753:
                IA8
                tour = 75328
            if tour == 7534691:
                IA8(T)
                print("Partie nulle!")
            turn = turn+1 
        if coup == 3 and t3[2] == " ":
            t3[2] = "O"
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
        if coup == 4 and t2[0] == " ":
            t2[0] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 745
            if tour == 791:
                IA3(T)
                tour = 7914
            if tour == 7532891:
                IA6(T)
                print("Partie nulle!")
            if tour == 753:
                IA6(T)
                tour = 75346
            turn = turn+1 
        if coup == 5 and t2[1] == " ":
            t2[1] = "O"
            Win(T)
            if tour == 0:
                IA3(T)
                tour = 753
            turn = turn+1 
        if coup == 6 and t2[2] == " ":
            t2[2] = "O"
            Win(T)
            if tour == 0:
                IA5(T)
                tour = 765
            if tour == 7538219:
                IA4(T)
                print("Partie nulle!")
            if tour == 753:
                IA4(T)
                tour = 75364
            turn = turn+1 
        if coup == 7 and t1[0] == " ":
            t1[0] = "O"
        if coup == 8 and t1[1] == " ":
            t1[1] = "O"
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
                print("Partie nulle!")
            turn = turn+1 
        if coup == 9 and t1[2] == " ":
            t1[2] = "O"
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
        print (" ",t0)
        print ("1",t1)
        print ("2",t2)
        print ("3",t3)
    return()


def IA1(T):
    t3[0] = "X"

def IA2(T):
    t3[1] = "X"

def IA3(T):
    t3[2] = "X"

def IA4(T):
    t2[0] = "X"

def IA5(T):
    t2[1] = "X"

def IA6(T):
    t2[2] = "X"

def IA7(T):
    t1[0] = "X"

def IA8(T):
    t1[1] = "X"

def IA9(T):
    t1[2] = "X"
        
def Win(T):
    if t1[0]=="X" and t1[1]=="X":
        if t1[2]== " ":
            t1[2]= "X"
            print ("Victoire de l'IA!") 
    if t1[0]==t1[2]=="X":
        if t1[1] == " ":
            t1[1]= "X"
            print ("Victoire de l'IA!")
    if t1[1]=="X" and t1[2]=="X":
        if t1[2] == " ":
            t1[0]= "X"
            print ("Victoire de l'IA!")
    if t2[0]=="X" and t2[1]=="X":
        if t2[2] == " ":
            t2[2]= "X"
            print ("Victoire de l'IA!")
    if t2[0]=="X" and t2[2]=="X":
        if t2[1] == " ":
            t2[1]= "X"
            print ("Victoire de l'IA!")
    if t2[1]=="X" and t2[2]=="X":
        if t2[0] == " ":
            t2[0]= "X"
            print ("Victoire de l'IA!")
    if t3[0]=="X" and t3[1]=="X":
        if t3[2] == " ":
            t3[2]= "X"
            print ("Victoire de l'IA!")
    if t3[0]=="X" and t3[2]=="X":
        if t3[1] == " ":
            t3[1]= "X"
            print ("Victoire de l'IA!")
    if t3[1]=="X" and t3[2]=="X":
        if t3[0] == " ":
            t3[0]= "X"
            print ("Victoire de l'IA!")
    if t1[0]=="X" and t2[1]=="X":
        if t3[2] == " ":
            t3[2]= "X"
            print ("Victoire de l'IA!")
    if t1[0]=="X" and t3[2]=="X":
        if t2[1] == " ":
            t2[1]= "X"
            print ("Victoire de l'IA!")
    if t2[1]=="X" and t3[2]=="X":
        if t1[0] == " ":
            t1[0]= "X"
            print ("Victoire de l'IA!")
    if t1[2]=="X" and t2[1]=="X":
        if t3[0] == " ":
            t3[0]= "X"
            print ("Victoire de l'IA!")
    if t1[2]=="X" and t3[0]=="X":
        if t2[1] == " ":
            t2[1]= "X"
            print ("Victoire de l'IA!")
    if t2[1]=="X" and t3[0]=="X":
        if t1[2] == " ":
            t1[2]= "X"
            print ("Victoire de l'IA!")
    if t1[0]=="X" and t2[0]=="X":
        if t3[0] == " ":
            t3[0]= "X"
            print ("Victoire de l'IA!")
    if t1[0]=="X" and t3[0]=="X":
        if t2[0] == " ":
            t2[0]= "X"
            print ("Victoire de l'IA!")
    if t2[0]=="X" and t3[0]=="X":
        if t1[0] == " ":
            t1[0]= "X"
            print ("Victoire de l'IA!")
    if t1[1]=="X" and t2[1]=="X":
        if t3[1] == " ":
            t3[1]= "X"
            print ("Victoire de l'IA!")
    if t1[1]=="X" and t3[1]=="X":
        if t2[1] == " ":
            t2[1]= "X"
            print ("Victoire de l'IA!")
    if t2[1]=="X" and t3[1]=="X":
        if t1[1] == " ":
            t1[1]= "X"
            print ("Victoire de l'IA!")
    if t1[2]=="X" and t2[2]=="X":
        if t3[2] == " ":
            t3[2]= "X"
            print ("Victoire de l'IA!")
    if t1[2]=="X" and t3[2]=="X":
        if t2[2] == " ":
            t2[2]= "X"
            print ("Victoire de l'IA!")
    if t2[2]=="X" and t3[2]=="X":
        if t1[2] == " ":
            t1[2]= "X"
            print ("Victoire de l'IA!")
    

changementJoueur(T)













































                          
