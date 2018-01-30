import random
print("Welcome to the classic Snake and Ladder Game!!!")
t=int(input("Select the type of game you want: \n 1. 1 Player \n 2. 2 Players \n"))
dice=0
score=0
score1=0
roll=0
dice1=0
if t==1:
    while score<=100:
        roll=int(input("\nPress 1 to roll: "))
        if roll==1:
            dice=random.randint(1,6)
            score=score+dice
            print("Your dice rolled to:",dice,"\nYou are in position:",score)
            if score==8:
                score=37
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==11:
                score=2
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==13:
                score=34
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==25:
                score=4
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==38:
                score=9
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==40:
                score=68
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==52:
                score=81
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==65:
                score=46
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==76:
                score=97
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==89:
                score=70
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==93:
                score=64
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==100:
                print("Congratulations! You won!!!")
                break
            if score>=100:
                score=score-dice
                if score==95:
                    if dice==6:
                        print("Can't move.")
                if score==96:
                    if (dice==6) or (dice==5):
                        print("Can't move.")
                if score==97:
                    if (dice==6) or (dice==5) or (dice==4):
                        print("Can't move.")
                if score==98:
                    if (dice==6) or (dice==5) or (dice==4) or (dice==3):
                        print("Can't move.")
                if score==99:
                    if (dice==6) or (dice==5) or (dice==4) or (dice==3) or (dice==2):
                        print("Can't move.")
        else:
            break
elif t==2:
    i=1
    while i==1:
        while score<=100 and score1<=100:
            roll=int(input("\nPlayer 1, press 1 to roll: "))
            if roll==1:
                dice=random.randint(1,6)
                score=score+dice
                print("Your dice rolled to:",dice,"\nYou are in position:",score)
                if score==8:
                    score=37
                    print("Oh Great! You got the ladder! :D You go to:",score)
                if score==11:
                    score=2
                    print("Oh No! A snake bit you! :( You fall back to:",score)
                if score==13:
                    score=34
                    print("Oh Great! You got the ladder! :D You go to:",score)
                if score==25:
                    score=4
                    print("Oh No! A snake bit you! :( You fall back to:",score)
                if score==38:
                    score=9
                    print("Oh No! A snake bit you! :( You fall back to:",score)
                if score==40:
                    score=68
                    print("Oh Great! You got the ladder! :D You go to:",score)
                if score==52:
                    score=81
                    print("Oh Great! You got the ladder! :D You go to:",score)
                if score==65:
                    score=46
                    print("Oh No! A snake bit you! :( You fall back to:",score)
                if score==76:
                    score=97
                    print("Oh Great! You got the ladder! :D You go to:",score)
                if score==89:
                    score=70
                    print("Oh No! A snake bit you! :( You fall back to:",score)
                if score==93:
                    score=64
                    print("Oh No! A snake bit you! :( You fall back to:",score)
                if score==100:
                    print("Congratulations! You won!!!")
                    i+=2
                    break
                if score>=100:
                    score=score-dice
                    if score==95:
                        if dice==6:
                            print("Can't move.")
                    if score==96:
                        if (dice==6) or (dice==5):
                            print("Can't move.")
                    if score==97:
                        if (dice==6) or (dice==5) or (dice==4):
                            print("Can't move.")
                    if score==98:
                        if (dice==6) or (dice==5) or (dice==4) or (dice==3):
                            print("Can't move.")
                    if score==99:
                        if (dice==6) or (dice==5) or (dice==4) or (dice==3) or (dice==2):
                            print("Can't move.")
            dice=0
            roll=int(input("\nPlayer 2, press 1 to roll: "))
            if roll==1:
                dice1=random.randint(1,6)
                score1=score1+dice1
                print("Your dice rolled to:",dice1,"\nYou are in position:",score1)
                if score1==8:
                    score1=37
                    print("Oh Great! You got the ladder! :D You go to:",score1)
                if score1==11:
                    score1=2
                    print("Oh No! A snake bit you! :( You fall back to:",score1)
                if score1==13:
                    score1=34
                    print("Oh Great! You got the ladder! :D You go to:",score1)
                if score1==25:
                    score1=4
                    print("Oh No! A snake bit you! :( You fall back to:",score1)
                if score1==38:
                    score1=9
                    print("Oh No! A snake bit you! :( You fall back to:",score1)
                if score1==40:
                    score1=68
                    print("Oh Great! You got the ladder! :D You go to:",score1)
                if score1==52:
                    score1=81
                    print("Oh Great! You got the ladder! :D You go to:",score1)
                if score1==65:
                    score1=46
                    print("Oh No! A snake bit you! :( You fall back to:",score1)
                if score1==76:
                    score1=97
                    print("Oh Great! You got the ladder! :D You go to:",score1)
                if score1==89:
                    score1=70
                    print("Oh No! A snake bit you! :( You fall back to:",score1)
                if score1==93:
                    score1=64
                    print("Oh No! A snake bit you! :( You fall back to:",score1)
                if score1==100:
                    print("Congratulations! You won!!!")
                    i+=2
                    break
                if score1>=100:
                    score1=score1-dice1
                    if score1==95:
                        if dice1==6:
                            print("Can't move.")
                    if score1==96:
                        if (dice1==6) or (dice1==5):
                            print("Can't move.")
                    if score1==97:
                        if (dice1==6) or (dice1==5) or (dice1==4):
                            print("Can't move.")
                    if score1==98:
                        if (dice1==6) or (dice1==5) or (dice1==4) or (dice1==3):
                            print("Can't move.")
                    if score1==99:
                        if (dice1==6) or (dice1==5) or (dice1==4) or (dice1==3) or (dice1==2):
                            print("Can't move.")
        else:
            break
