SIZE = 80 # matrix is 80x80

with open('./Text Files/0081_matrix.txt', 'r') as p81:
    p81matrix = p81.read()

matrix = []
for row in p81matrix.split('\n')[:-1]: # don't include the last element as it is just a newline character
    appendarr = []
    for s in row.split(','):
        appendarr.append(int(s))
    matrix.append(appendarr)

opening = [] # contains arrays of diagonal (top right tilt) values with lengths incrementing from 1 to 80 (inclusive)
for i in range(SIZE): # i represents steps from beginning
    row = []
    for k in range(i + 1): # k will be the column we are selecting
        row.append(matrix[i - k][k]) # total amount of steps down/right must be i steps, row will append values along the top right tilt diagonal

    opening.append(row)

ending = [] # contains arrays of diagonal (top right tilt) values with lengths decrementing from 79 to 1 (inclusive) | second half of opening[]
for i in range(SIZE - 1): # i represents steps from ending, will run 79 times instead of 80
    row = []
    for k in range(i + 1):
        row.append(matrix[-k - 1][k - i - 1]) # negative values of indexes in line 17 (minus 1 to change 0-indexing for negatives which are 1-indexed)
    # taking the negative of both axes whill swap the top right and bottom left corners (like a transpose)
    # hence also swapped places of coordinates to keep the same orientation of the axes
    # will just get values from the opposite corner (bottom right) but same diagonal (top right tilt)
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
print(min(pathSum([minBelowSums, minAboveSums])))
# the order of minAboveSums/minBelowSums doesn't matter here as paths can go from start to end or vice versa, so just use the order that can fit into the function