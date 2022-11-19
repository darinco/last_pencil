pencils = input('How many pencils would you like to use: \n')
flag = True
while flag:
    if pencils.isdigit():
        pencils = int(pencils)
        if pencils <= 0:
            pencils = input('The number of pencils should be positive \n')
        else:
            flag = False
    else:
        pencils = input('The number of pencils should be numeric \n')

player = input('Who will be the first (John, Jack): \n').title()
while player != 'John' and player != 'Jack':
    player = input('Choose between John and Jack \n').title()

while pencils > 0:
    print('|' * pencils)
    print(f'{player}\'s turn: (you can take from 1 to 3 pencils)')

    if player == 'John':
        n = input()
        try_again = True
        while try_again:
            if n.isdigit() and 1 <= int(n) <= 3:
                n = int(n)
                if n > pencils:
                    n = input('Too many pencils were taken \n')
                try_again = False
            else:
                n = input("Possible values: '1', '2' or '3' \n")
        player = 'Jack'

    else:
        if pencils % 4 == 0:
            n = 3
        elif pencils % 4 == 1:
            n = 1
        else:
            n = pencils % 4 - 1
        print(n)
        player = 'John'

    pencils = pencils - int(n)

print(f'{player} won!')
