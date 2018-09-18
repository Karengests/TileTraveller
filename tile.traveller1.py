#https://github.com/Karengests/TileTraveller/blob/master/tile.traveller1.py
x = 1
y = 1
tile = (x,y)

while tile != (3,3)
    print("You can Travel:", end='')
    if tile == (1,1): 
        print("You can travel: (N)orth")
           
    elif tile == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")

    elif tile == (1,3):
        print("You can travel: (S)outh or (E)east")

    elif tile == (2,1):
        print("You can travel: (N)orth")

    elif tile == (2,2):
        print("You can travel: (S)outh or (W)est")

    elif tile == (2,3):
        print("You can travel: (W)est or (E)ast")

    elif tile == (3,1):
        print("Victory!")

    elif tile == (3,2):
        print("You can travel: (N)orth")

    elif tile == (3,3):
        print("You can travel: (S)outh or (W)est")

    direction = input(str("Input a direction: "))



    