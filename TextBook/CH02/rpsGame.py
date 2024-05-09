import random, sys
print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0
i = 0
j = 0

while True:
    print(str(wins)+ ' Wins,' +str(losses)+' Losses,'+str(ties)+' Ties')

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Type one of r, p, s, or q')

    if player_move == 'r':
        print('ROCK versus...')
        i += 1
    elif player_move == 'p':
        print('PAPER versus...')
        i += 2
    elif player_move == 's':
        print('SCISSORS versus...')
        i += 3

    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
        j += 1
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
        j += 2
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')
        j += 3

    if player_move == computer_move:
        print('It is a tie')
        ties += 1
        i *= 0 
        j *= 0
    elif (i == 1 and j ==3) or (i == 2 and j == 1) or (i == 3 and j == 2):
        print('You WIN')
        wins += 1
        i *= 0
        j *= 0
    elif (i == 1 and j ==2) or (i == 2 and j == 3) or (i == 3 and j == 1):
        print('You LOSE')
        losses += 1
        i *= 0
        j *= 0

