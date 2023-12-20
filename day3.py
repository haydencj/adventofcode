from sys import argv
# 10 columns 10 rows

# 467 (0, 0) adjacent to * (1, 3)
# 7 in 467 is (0, 2)
symbols = ['*', '#', '+', '$']

# create algorithm to check if number has a symbol adjacent to that coord
def checkAdjacent(coords, file):
    for x, line in enumerate(file): # row
        for y, char in enumerate(line): # column
            # use switch case instead of ifs?
            if tuple((x, y+1)) in coords and char != '.':
                print(f"{char}: ({x}, {y})")
            

# assign every symbol a x and y value
def getCoords(file):
    # use tuple for coords, and list for array of coords
    coords = list()

    for x, line in enumerate(file): # row
        for y, char in enumerate(line): # column
            if char in symbols:
                coords.append(tuple((x,y)))

    file.seek(0)
    return coords

if __name__ == '__main__':
    coords = list()

    with open(argv[1], 'r') as file:
        coords = getCoords(file)
        checkAdjacent(coords, file)

    print(coords)
