#Assignment 8
#https://github.com/Fridrikjonsson/TileTraveller.git

x = 1
y = 1
upp = "n" or "N"
nidur = "s" or "S"
haegri = "e" or "E"
vinstri = "w" or "W"
#att = str(input("Direction: "))

#start tile 1,1
print("You can travel: (N) orth")
att = str(input("Direction: "))
if att != upp:
    print("Not a valid direction!")
else:
    y = y + 1
#tile 1,2
if x == 1 and y == 2:
    print("You can travel: (N) orth or (E) ast or (S) outh.")
    att = str(input("Direction: "))
    if att == upp:
        y = y + 1
    elif att == haegri:
        x = x + 1
    elif att == nidur:
        y = y - 1
    else:
        print("Not a valid direction!")
#tile 2,2
if x == 2 and y == 2:
    print("You can travel: (W) est or (S) outh.")
    att = str(input("Direction: "))
    if att == vinstri:
        x = x - 1
    elif att == nidur:
        y = y - 1
    elif att != vinstri or nidur:
        print("Not a valid direction!")
#tile 2,1
if x == 2 and y == 1:
    print("You can travel: (N) orth.")
    att = str(input("Direction: "))
    if att != upp:
        print("Not a valid direction!")
    else:
        y = y + 1
#tile 1,3
if x == 1 and y == 3:
    print("You can travel: (E) ast or (S) outh.")
    att = str(input("Direction: "))
    if att == haegri:
        x = x + 1
    elif att == nidur:
        y = y - 1
    elif att != haegri or nidur:
        print("Not a valid direction!")
#tile 2,3
if x == 2 and y == 3:
    print("You can travel: (E) ast or (W) est.")
    att = str(input("Direction: "))
    if att == haegri:
        x = x + 1
    elif att == vinstri:
        x = x - 1
    elif att != haegri or vinstri:
        print("Not a valid direction!")
#tile 3,3
if x == 3 and y == 3:
    print("You can travel: (W) est or (S) outh.")
    att = str(input("Direction: "))
    if att == vinstri:
        x = x - 1
    elif att == nidur:
        y = y - 1
    elif att != vinstri or nidur:
        print("Not a valid direction!")
#tile 3,2
if x == 3 and y == 2:
    print("You can travel: (N) orth or (S) outh.")
    att = str(input("Direction: "))
    if att == upp:
        y = y + 1
    elif att == nidur:
        y = y - 1
        print("Victory!")
    elif att != upp or nidur:
        print("Not a valid direction!")