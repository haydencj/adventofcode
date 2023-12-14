from sys import argv

def calc_game(game: str) -> int:
    cubes = {'red': 12, 'blue': 14, 'green': 13} # number of cubes in bag
    min_cubes = {'red': 0, 'blue': 0, 'green': 0}

    game = game.split(':') 
    id = game[0].split()[1] # get game id
    sets = game[1].split(';') # get list of sets

    for set in sets: # each set per game
        for draw in set.split(','): # each draw per set
            
            draw = draw.lstrip()
            num, color = draw.split()

            # check for min here
            if int(num) > min_cubes[color]:
                min_cubes[color] = int(num)

            # part 1
            # if int(num) > cubes[color]: # game not possible
            #     return 0

    power = min_cubes['red'] * min_cubes['blue'] * min_cubes['green']

    print(min_cubes)
    print(power)

    return power # game is possible return id
 
if __name__ == '__main__':
    powers = list()

    with open(argv[1], 'r') as file:
        for game in file:
            powers.append( calc_game(game.strip()) )
        
        powersSum = sum(powers)
        print(powersSum)