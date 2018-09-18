tile = 1,1

while
    if tile == "1,1": 
        print("You can travel: ", N)
        direction = input(str("Direction: "))

        if direction == "n" or "N":
            print("You can travel: N(orth).")
        else:
            print("Not valid direction!")


    elif tile == "1,2":
        print("You can travel: ",N, S, E)

    elif tile == "1,3":
        print("You can travel: ", S, E)

    elif tile == "2,1":
        print("You can travel: ", N)

    elif tile == "2,2":
        print("You can travel: ", S, W)

    elif tile == "2,3":
        print("You can travel: ", W, E)

    elif tile == "3,1":
        print("You can travel: ", N)

    elif tile == "3,2":
        print("You can travel: ", N )

    elif tile == "3,3":
        print("You can travel: ", S, W)
