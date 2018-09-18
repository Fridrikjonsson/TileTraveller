#Byrja á því að búa til svæðið sem leikmaðurinn er í, leyfa leikmanninum að færa sig í átt sem hægt er að færa sig í. Setja síðan inn 
#markmiðið, staðinn sem leikmaðurinn þarf að komast til að vinna
#https://github.com/Fridrikjonsson/TileTraveller.git
position = 1.1
att = "(N)orth."
villa = 0
while position != 3.1:
    if villa == 1:
        direction = input("Direction: ").lower()
        villa = villa - 1
    else:
        print("You can travel:", att)
        direction = input("Direction: ").lower()
    if direction == "n":
        if position == 1.1 or position == 1.2 or position == 3.2 or position == 2.1:
            position = position + 0.1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    elif direction == "s":
        if position == 1.2 or position == 1.3 or position == 2.2 or position == 3.3 or position == 3.2:
            position = position - 0.1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    elif direction == "w":
        if position == 2.3 or position == 2.2 or position == 3.3:
            position = position - 1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    elif direction == "e":
        if position == 1.2 or position == 1.3 or position == 2.3:
            position = position + 1
        else:
            print("Not a valid direction!")
            villa = villa + 1
    else:
        print("Not a valid direction!")
        villa = villa + 1
    position = round(position, 1)
    if position == 1.1:
        att = "(N)orth."
    if position == 1.2:
        att = "(N)orth or (E)ast or (S)outh."
    if position == 1.3:
        att = "(E)ast or (S)outh."
    if position == 2.1:
        att = "(N)orth."
    if position == 2.2:
        att = "(S)outh or (W)est."
    if position == 2.3:
        att = "(E)ast or (W)est."
    if position == 3.1:
        att = "(N)orth."
    if position == 3.2:
        att = "(N)orth or (S)outh."
    if position == 3.3:
        att = "(S)outh or (W)est."
print("Victory!")
