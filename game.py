#Rock paper and scissors game
import random
def game(comp,player):
    if comp==player:
        return none

    elif comp=='r':
        if player=='p':
            return true
        elif player=='s':
            return false

    elif comp == 'p':
        if player == 's':
            return true
        elif player == 'r':
            return false

    elif comp == 's':
        if player == 'p':
            return true
        elif player == 'r':
            return false



print("Computer's Turn:Choose Rock(r),Paper(p),Scissor(s)  ")
randomno=random.randint(1,3)
if randomno==1:
    comp='r'
elif randomno==2:
    comp='p'
elif randomno==3:
    comp='s'
player=input("Player's Turn:Choose Rock(r),Paper(p),Scissor(s)?  ")

a = game(comp,player)
if a==none:
    print("The Game is Tie..!!")
elif a==true:
    print("You Win The Game...!!  Congrats!!!")
else:
    print("You Lost The Game :( ")