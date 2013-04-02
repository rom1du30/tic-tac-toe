#Projet BAC ISN



t0 = ["A","B","C"]
t1 = [" "]*3
t2 = [" "]*3
t3 = [" "]*3




def player1(t0,t1,t2,t3):
                    coup = int(input("Quel est votre coup?"))
                    if coup == 1 and t3[0] == " ":
                        t3[0] = "O"
                    if coup == 2 and t3[1] == " ":
                        t3[1] = "O"
                    if coup == 3 and t3[2] == " ":
                        t3[2] = "O"
                    if coup == 4 and t2[0] == " ":
                        t2[0] = "O"
                    if coup == 5 and t2[1] == " ":
                        t2[1] = "O"
                    if coup == 6 and t2[2] == " ":
                        t2[2] = "O"
                    if coup == 7 and t1[0] == " ":
                        t1[0] = "O"
                    if coup == 8 and t1[1] == " ":
                        t1[1] = "O"
                    if coup == 9 and t1[2] == " ":
                        t1[2] = "O"   
                    print (" ",t0)
                    print ("1",t1)
                    print ("2",t2)
                    print ("3",t3)
                    

def player2(t0,t1,t2,t3):
                    coup = int(input("Quel est votre coup?"))
                    if coup == 1 and t3[0] == " ":
                        t3[0] = "X"
                    if coup == 2 and t3[1] == " ":
                        t3[1] = "X"
                    if coup == 3 and t3[2] == " ":
                        t3[2] = "X"
                    if coup == 4 and t2[0] == " ":
                        t2[0] = "X"
                    if coup == 5 and t2[1] == " ":
                        t2[1] = "X"
                    if coup == 6 and t2[2] == " ":
                        t2[2] = "X"
                    if coup == 7 and t1[0] == " ":
                        t1[0] = "X"
                    if coup == 8 and t1[1] == " ":
                        t1[1] = "X"
                    if coup == 9 and t1[2] == " ":
                        t1[2] = "X"   
                    print (" ",t0)
                    print ("1",t1)
                    print ("2",t2)
                    print ("3",t3)
                    

x = 0
while x < 10:
    if x%2 == 0:
        player1(t0,t1,t2,t3)
    if x%2 == 1:
        player2(t0,t1,t2,t3)
    x = x+1
    

    

    
    


