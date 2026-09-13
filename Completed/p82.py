with open('./Text Files/0082_matrix.txt', 'r') as p82:
    p82matrix = [row for row in p82.read().split('\n') if len(row) > 0]

matrix = [] # 80x80 matrix
for row in p82matrix:
    matrix.append([int(s) for s in row.split(',')])

minimalPaths = [[-1 for _ in range(len(matrix))] for _ in range(len(matrix))] # there are only positive values, so -1 cannot be reached, -1 will represent an unchecked cell
# minimalPaths[] will return the minimal path sum, NOT INCLUDING THE CELL ITSELF, only the sum of path cells AFTER the referenced cell
# whether the initial cell is included or not is arbitrary, you can simply adjust the code to your whims

for col in range(len(matrix[0]) - 1, -1, -1): # run minPathSum() in the last column, then move leftwards and run through every column
    for row in range(len(matrix)): # iterate through each row
        if col == len(matrix[0]) - 1:
            minimalPaths[row][col] = 0 # at last column, there is no following path
            continue

        # logic: find minimal destination cell in the next column (1 col to the right) and move leftwards until the overall minimal is found

        minPath = matrix[row][col + 1] + minimalPaths[row][col + 1] # assume best path is through cell on the right

        pathSum = matrix[row][col + 1] # first cell in the path (path is guaranteed to include cell to the right of the origin)
        for r in range(row - 1, -1, -1): # move upward in rows, only count rows strictly above
            pathSum += matrix[r][col + 1] # add current cell value (adds together and is included in the sum since it is not the origin)
            if pathSum + minimalPaths[r][col + 1] < minPath: minPath = pathSum + minimalPaths[r][col + 1]

        pathSum = matrix[row][col + 1]
        for r in range(row + 1, len(matrix)): # move downward in rows, only count rows strictly below
            pathSum += matrix[r][col + 1]
            if pathSum + minimalPaths[r][col + 1] < minPath: minPath = pathSum + minimalPaths[r][col + 1]

        minimalPaths[row][col] = minPath # minPath is found, record it in minimalPaths[]

print(min(matrix[i][0] + minimalPaths[i][0] for i in range(len(matrix)))) # add origin value itself as minimalPaths[] does not include origin value