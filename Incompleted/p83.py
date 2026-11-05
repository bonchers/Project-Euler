with open('./Text Files/0083_matrix.txt', 'r') as p83:
    p83matrix = p83.read()

matrix = []
for row in p83matrix.split('\n')[:-1]: # don't include the last row as it is just a newline character
    appendrow = []
    for s in row.split(','):
        appendrow.append(int(s))
    matrix.append(appendrow)

matrix = [[131,673,234,103,18],
          [201, 96,342,965,150],
          [630,803,746,422,111],
          [537,699,497,121,956],
          [805,732,524,37,331]]

# s = 10
# mtrix = matrix.copy()
# matrix = [[mtrix[row][col] for col in range(s)] for row in range(s)]

SIZE = len(matrix) # matrix is 80x80

'''
logic:
move the path downwards (or turn direction anti-clockwise if at border or proceeding into already fully checked tile) until bottom-right reached
step backwards until the last non-fully checked tile, if all 4 surrounding tiles are fully checked (less tiles if at border),
set minPath of the tile as value + smallest surrounding minPath
otherwise, continue checking the other possible paths starting from latest non-fully checked tile in the path

if a tile is reached where there is no possible way to reach end without repeating tiles (loop is formed, and loops are redundant, so path is not min),
step backwards
'''

# XXX 'surrounding tiles' will refer to tiles that are directly adjacent to a tile; above, below, or beside it; not any diagonal tiles

minPaths = [[-1 for _ in range(SIZE)] for _ in range(SIZE)] # -1 represents minPath not found

minPaths[-1][-1] = matrix[-1][-1] # minPath of bottom right corner (destination tile) is itself
minPaths[-1][-2] = matrix[-1][-2] + matrix[-1][-1] # all tiles are positive, 
minPaths[-2][-1] = matrix[-2][-1] + matrix[-1][-1] # so minimal path of the 2 tiles surrounding destination is straight to destination

surrounding = lambda c: [(c[0] + 1, c[1]), (c[0], c[1] + 1), (c[0] - 1, c[1]), (c[0], c[1] - 1)] # [down, right, up, left]
#import sys
#sys.setrecursionlimit(100000)

def findPath(curr = (0, 0), path = []): # curr is a tuple of (row, col) coords of current tile, path is an array of coords of previous tiles in the path
    if minPaths[curr[0]][curr[1]] != -1: return [minPaths[curr[0]][curr[1]]] # prevent re-checking already fully checked tiles
    if curr in path: return []

    nextPathSums = []
    for surrCoord in surrounding(curr): # adjacent tiles to current tile
        if min(surrCoord) < 0 or max(surrCoord) >= SIZE: continue # prevent coords from exceeding borders (0 to SIZE - 1) (inclusive)
        #print(surrCoord, path + [curr])

        for nextSurr in surrounding(surrCoord):
            touchingPath = 0
            if nextSurr in path + [curr]: touchingPath += 1
        if touchingPath >= 2: return [] # surrounding includes previous tile & another tile: redundant as you could just travel to that node earlier instead of roundabout then touching
        
        nextPathSums += findPath(surrCoord, path + [curr]) # empty array represents no solution, automatically not included

    if len(nextPathSums) > 0:
        minNext = min(nextPathSums)
        if len(nextPathSums) == 4: # all 4 surrounding (adjacent) tiles are fully checked
            minPaths[curr[0]][curr[1]] = matrix[curr[0]][curr[1]] + minNext # record minimal path in minPaths[]
            #print(minPaths[curr[0]][curr[1]], curr)
        return [matrix[curr[0]][curr[1]] + minNext] # return minimum

    return [] # return empty array if no solutions from this current path

print(findPath())

''' XXX Code from p81.py XXX
opening = [] # contains arrays of diagonal (bottom left to top right // upward slope) values with lengths incrementing from 1 to 80 (inclusive)
for i in range(SIZE): # i represents steps from beginning
    row = []
    for k in range(i + 1): # k will be the column we are selecting
        row.append(matrix[i - k][k]) # total amount of steps down/right must be i steps, row will append values along the upward slope diagonal

    opening.append(row)

ending = [] # contains arrays of diagonal (upward slope) values with lengths decrementing from 79 to 1 (inclusive) | second half of opening[]
for i in range(SIZE - 1): # i represents steps from ending, will run 79 times instead of 80
    row = []
    for k in range(i + 1):
        row.append(matrix[-k - 1][k - i - 1]) # negative values of indexes in line 17 (minus 1 to change 0-indexing for negatives which are 1-indexed)
    # taking the negative of both axes whill swap the top right and bottom left corners (like a transpose)
    # hence also swapped places of coordinates to keep the same orientation of the axes
    # will just get values from the opposite corner (bottom right) but same diagonal (upward slope)
    ending.append(row)

# opening[] is now an array of possible positions after a certain amount of steps. opening[0] for after 0 steps, opening[3] for after 3 steps, and so on.
# for every element's index i in opening[n], the NEXT element (after a step) can be opening[n + 1][i] or opening[n + 1][i + 1]

# ending[] is the same as opening[] but ending[i] is for i steps from the end
# for every element's index i in ending[n], the PREVIOUS element (one step before) can be ending[n + 1][i] or ending[n + 1][i + 1]

# calculate path sum for paths leading to and coming from the middle diagonal
# paths leading to middle (from top left) will reach the exact middle, with 80 elements along the diagonal
# paths coming from the middle (to bottom right) will come directly before the middle, with 79 elements along the diagonal

def pathSum(paths): # arrays in paths[] must increment in length as the index increments, i.e. lengths go like n, n+1, n+2, ... 
    arr = paths[0]
    for row in paths[1:]: # arr is already paths[0], so don't count it twice, start from index 1
        newarr = []
        for i in range(len(row)):
            if i == 0: newarr.append(arr[0] + row[i])
            elif i == len(row) - 1: newarr.append(arr[-1] + row[i])
            else: newarr.append(min(arr[i - 1], arr[i]) + row[i])

        arr = newarr
    return arr

minAboveSums = pathSum(opening)
minBelowSums = pathSum(ending)
print(min(pathSum([minBelowSums, minAboveSums])))'''