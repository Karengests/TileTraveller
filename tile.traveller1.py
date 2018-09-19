tile = (1,1)

direct = '(N)orth.'
print('You can travel: ',direct)

while tile != (3,1):

    if tile == (1,1): 
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            tile = (1,2)
            direct = '(N)orth or (E)ast or (S)outh.'
            print('You can travel:',direct)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            tile = tile
           
    elif tile == (1,2):
        if direction == 'n' or direction =='N':
            tile = (1,3)
            direct = '(E)ast or (S)outh.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        elif direction == 'e' or direction == 'E':
            tile = (2,2)
            direct = '(S)outh or (W)est.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        elif direction == 's' or direction =='S':
            tile = (1,1)
            direct = '(N)orth.'
            print('You can travel:',direct)
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')

    elif tile == (1,3):
        if direction == 's' or direction == 'S':
            tile = (1,2)
            direct = '(N)orth or (E)ast or (S)outh.'
            print('You can travel:',direct)
            direction = input('Direction: ')
        elif direction == 'e' or direction =='E':
            tile = (2,3)
            direct = '(E)ast or (W)est.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')


    elif tile == (2,1):
        if direction == 'n' or direction =='N':
            tile = (2,2)
            direct = '(S)outh or (W)est.'    
            print('You can travel:',direct)
            direction = input('Direction: ')    
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')

    elif tile == (2,2):
        if direction == 's' or direction == 'S':
            tile = (2,1)
            direct = '(N)orth.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        elif direction == 'w' or direction == 'W':
            tile = (1,2)  
            direct = '(N)orth or (E)ast or (S)outh.'
            print('You can travel:',direct)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')

    elif tile == (2,3):
        if direction == 'e' or direction =='E':
            tile = (3,3)
            direct = '(S)outh or (W)est.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        elif direction == 'w' or direction =='W':
            tile = (1,3)
            direct = '(E)ast our (S)outh.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')

    elif tile == (3,2):
        if direction == 's' or direction == 'S':
            tile = (3,1) 
        elif direction == 'n' or direction == 'N':
            tile = (3,3)
            direct = '(S)outh or (W)est.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')

    elif tile == (3,3):
        if direction == 'w' or direction =='W':
            tile = (2,3)
            direct = '(E)ast or (W)est.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        elif direction == 's' or direction == 'S':
            tile = (3,2)
            direct = '(N)orth or (S)outh.'    
            print('You can travel:',direct)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            tile = tile
            direction = input('Direction: ')
            
    if tile == (3,1):
        print("Victory!")
    



    