#Setja áttir sem variable
#búa til if setningu fyrir hvern reit

#https://github.com/Fridrikjonsson/TileTraveller.git

x = 1
y = 1
upp = "n" or "N"
nidur = "s" or "S"
haegri = "e" or "E"
vinstri = "w" or "W"
aftur = True

while not (x == 3 and y == 1):
#start tile 1,1
    if x == 1 and y == 1:
        if aftur == True:
            print("You can travel: (N)orth")
        att = input("Direction: ").lower()
        if att == upp:
            y = y + 1
        else:
            print("Not a valid direction!")
            aftur = False
#tile 1,2
    if x == 1 and y == 2:
        if aftur == True:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        att = input("Direction: ").lower()
        if att == upp:
            y = y + 1
        elif att == haegri:
            x = x + 1
        elif att == nidur:
            y = y - 1
        else:
            print("Not a valid direction!")
            aftur = False
#tile 2,2
    if x == 2 and y == 2:
        if aftur == True:
            print("You can travel: (W)est or (S)outh.")
        att = input("Direction: ").lower()
        if att == vinstri:
            x = x - 1
        elif att == nidur:
            y = y - 1
        elif att != vinstri or nidur:
            print("Not a valid direction!")
            aftur = False
#tile 2,1
    if x == 2 and y == 1:
        if aftur == True:
            print("You can travel: (N)orth.")
        att = input("Direction: ").lower()
        if att != upp:
            print("Not a valid direction!")
            again = False
        elif att == upp:
            y = y + 1
#tile 1,3
    if x == 1 and y == 3:
        if aftur == True:
            print("You can travel: (E)ast or (S)outh.")
        att = input("Direction: ").lower()
        if att == haegri:
            x = x + 1
        elif att == nidur:
            y = y - 1
        elif att != haegri or nidur:
            print("Not a valid direction!")
            aftur = False
#tile 2,3
    if x == 2 and y == 3:
        if aftur == True:
            print("You can travel: (E)ast or (W)est.")
        att = input("Direction: ").lower()
        if att == haegri:
            x = x + 1
        elif att == vinstri:
            x = x - 1
        elif att != haegri or vinstri:
            print("Not a valid direction!")
            aftur = False
#tile 3,3
    if x == 3 and y == 3:
        if aftur == True:
            print("You can travel: (W)est or (S)outh.")
        att = input("Direction: ").lower()
        if att == vinstri:
            x = x - 1
        elif att == nidur:
            y = y - 1
        elif att != vinstri or nidur:
            print("Not a valid direction!")
            aftur = False
#tile 3,2
    if x == 3 and y == 2:
        if aftur == True:
            print("You can travel: (N)orth or (S)outh.")
        att = input("Direction: ").lower()
        if att == upp:
            y = y + 1
        elif att == nidur:
            y = y - 1
            print("Victory!")
        elif att != upp or nidur:
            print("Not a valid direction!")
            aftur = False
