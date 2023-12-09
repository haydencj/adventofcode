from sys import argv

def calc_game(game: str) -> int:
    cubes = {'red': 12, 'blue': 13, 'green': 14} # number of cubes in bag

    match = game.split(':')
    id = match[0].split()[1]

    sets = match[1].split(';')

    for set in sets: # each set per game
        for draw in set.split(','): # each draw per set

            draw = draw.lstrip()
            num, color = draw.split()

            if int(num) > cubes[color]: # game not possible
                print(id)
                return 0
            
    return int(id) # game is possible return id

if __name__ == '__main__':
    ids = list()

    with open(argv[1], 'r') as file:
        for game in file:
            ids.append( calc_game(game.strip()) )
        
        idSum = sum(ids)
        print(idSum)