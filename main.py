import random

def gamewin(comp, you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        elif comp == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        elif comp == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif comp == 'w':
            return True

name = input("enter your name :- ")

print("computer turn: Snake(s) Water(w) or Gun(g)? ")

randNO = random.randint(1, 3)
if randNO == 1:
    comp = "s"
elif randNO == 2:
    comp = "w"
elif randNO == 3:
    comp = "g"
you = input("your turn: Snake(s) Water(w) or Gun(g) ?")

a = gamewin(comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("game is tie: ")
elif a:
    print(f"{name} you win: ")
else:
    print(f"{name} you loose: ")























