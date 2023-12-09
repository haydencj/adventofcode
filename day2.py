from sys import argv

def calc_game(game: str) -> int:
    cubes = {'red': 12, 'blue': 13, 'green': 14} # number of cubes in bag
    cubesPerGame = dict()

    match = game.split(':')
    id = match[0].split()[1]

    sets = match[1].split(';')

    #print(sets)

    for set in sets:
        #print(set)
        for pulled in set.split(','):

            pulled = pulled.lstrip()
            num, color = pulled.split()
            #print(pulled)

            if int(num) > cubes[color]: # game not possible
                print(id)
                return 0
            
    # game is possible return id
    return int(id)

if __name__ == '__main__':
    ids = list()

    with open(argv[1], 'r') as file:
        for game in file:
            ids.append( calc_game(game.strip()) )
        
        print(ids)
        idSum = sum(ids)
        print(idSum)