import random
print("Welcome to the classic Snake and Ladder Game!!!")
t=int(input("Select the type of game you want: \n 1. 1 Player \n 2. 2 Players \n"))
dice=0
temp=0
if t==1:
    while temp<=100:
        roll=int(input("Press 1 to roll: "))
        if roll==1:
            dice=random.randint(1,6)
            temp=temp+dice
            temp1=temp
            print("Your dice rolled to:",dice,"\nYou are in position:",temp)
            if temp==8:
                temp=37
                print("Oh Great! You got the ladder! :D You go to:",temp)
            if temp==11:
                temp=2
                print("Oh No! A snake bit you! :( You fall back to:",temp)
            if temp==13:
                temp=34
                print("Oh Great! You got the ladder! :D You go to:",temp)
            if temp==25:
                temp=4
                print("Oh No! A snake bit you! :( You fall back to:",temp)
            if temp==38:
                temp=9
                print("Oh No! A snake bit you! :( You fall back to:",temp)
            if temp==40:
                temp=68
                print("Oh Great! You got the ladder! :D You go to:",temp)
            if temp==52:
                temp=81
                print("Oh Great! You got the ladder! :D You go to:",temp)
            if temp==65:
                temp=46
                print("Oh No! A snake bit you! :( You fall back to:",temp)
            if temp==76:
                temp=97
                print("Oh Great! You got the ladder! :D You go to:",temp)
            if temp==89:
                temp=70
                print("Oh No! A snake bit you! :( You fall back to:",temp)
            if temp==93:
                temp=64
                print("Oh No! A snake bit you! :( You fall back to:",temp)
            elif temp==95:
                if dice==6:
                    temp=temp1-dice
                    print("Can't move.")
            elif temp==96:
                if (dice==6) or (dice==5):
                    temp=temp1-dice
                    print("Can't move.")
            elif temp==97:
                if (dice==6) or (dice==5) or (dice==4):
                    temp=temp1-dice
                    print("Can't move.")
            elif temp==98:
                if (dice==6) or (dice==5) or (dice==4) or (dice==3):
                    temp=temp1-dice
                    print("Can't move.")
            elif temp==99:
                if (dice==6) or (dice==5) or (dice==4) or (dice==3) or (dice==2):
                    temp=temp1-dice
                    print("Can't move.")
            elif temp==100:
                print("Congratulations! You won!!!")
            if temp>=100:
                break
        else:
            break
