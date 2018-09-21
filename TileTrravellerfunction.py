#1. Which implementation was easier and why?
#2. Which implementation is more readable and why?
#3. Which problems in the first implementations were you able to solve with the latter implementation?
#1. Mér fannst fyrsta einfaldara en það er út af því ég þurfti að endurgera með functions sem gékk hægar.
#2. Fyrsta er meiri readable hjá mér en hefði ég notað functions á öðrum hætti væri það betra.
#3. Það er einfaldara að bæta við reiti og body-ið á kóðanum er mun styttri.

#https://github.com/Fridrikjonsson/TileTraveller.git
def reitur(x,y):
    if x == 1:
        if y == 1:
            stadsetning = "1000"
        if y == 2:
            stadsetning = "1110"
        if y == 3:
            stadsetning = "0110"
    if x == 2:
        if y == 1:
            stadsetning = "1000"
        if y == 2:
            stadsetning = "0011"
        if y == 3:
            stadsetning = "0101"
    if x == 3:
        if y == 1:
            stadsetning = "5555"
        if y == 2:
            stadsetning = "1010"
        if y == 3:
            stadsetning = "0011"
    return stadsetning
def attir(stad):
    print("You can travel:",end="")
    if stad[0]=='1':
        N=True
        print(" (N)orth", end="")
    else:
        N=False
    if stad[1]=='1':
        E=True
        if N==True:
            print(" or", end="")
        print(" (E)ast", end="")
    else:
        E=False
    if stad[2]=='1':
        S=True
        if N==True or E==True:
            print(" or", end="")
        print(" (S)outh", end="")
    else:
        S=False
    if stad[3]=='1':
        W=True
        if N==True or E==True or S==True:
            print(" or", end="")
        print(" (W)est", end="")
    else:
        W=False
    print(".")
    return N,E,S,W
def stadsetningk(x,y,N,E,S,W):
    again = True
    att=input("Direction: ").lower()
    if att=="n" and N==True:
        y = y+1
    elif att=="e" and E==True:
        x = x+1
    elif att=="s" and S==True:
        y = y-1
    elif att=="w" and W==True:
        x = x-1
    else:
        print("Not a valid direction!")
        again=False
    return(x,y,again)

x = 1
y = 1
N = False
E = False
S = False
W = False
win = False
again = True

while win == False:
    stadsetning = reitur(x,y)
    if stadsetning =="5555":
        print("Victory!")
        win = True
    else:
        if again == True:
            t_or_f = attir(stadsetning)
            N=t_or_f[0]
            E=t_or_f[1]
            S=t_or_f[2]
            W=t_or_f[3]
        temp = stadsetningk(x,y,N,E,S,W)
        x=temp[0]
        y=temp[1]
        again=temp[2]