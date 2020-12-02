import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True
    elif comp =='w':
        if you =='g':
            return False
        elif you =='s':
            return True
    elif comp =='g':
        if you =='s':
            return False
        elif you =='w':
            return True


print("Computer's turn : Snake(s), or Water(w), or Gun(g)\n")
randNO = random.randint(1, 3)
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

print("Computer has choosen his move now your turn:\n")
you = input("Your turn : Snake(s), or Water(w), or Gun(g)\n")

acd = gameWin(comp, you)
if acd == True:
    print('WoW, You won the match\n') 
elif acd == False:
    print("Oh, You lose the match\n")
else:
    print('Its a tie between you and the computer\n')

print(f"The computer choosed {comp}")