with open('./Text Files/0096_sudoku.txt', 'r') as p96:
    p96sudoku = p96.read().split('\n')

sudokuArr = [[] for _ in range(50)] # 0096_sudoku.txt has 50 Sudoku grids | sudoku[n][r][c] is the nth grid, rth row, cth column (both from top left) (0-indexed)
sudokuNo = -1
for i in range(len(p96sudoku)):
    if i % 10 == 0:
        sudokuNo += 1
        continue
    sudokuArr[sudokuNo].append([int(n) for n in p96sudoku[i]])

# game plan: for each cell, list all numbers it can be (check row, column, 3x3 box), if only 1 number remains, then the number is found for that cell
# after going through the 9x9 grid, if a cell is the only one in its row/column/box than can be a number n, then the cell is n
# check if solved (there are no more zeroes), if not solved, repeat

def getCell(grid, row, col): # returns array of values the cell could be
    colNums = [grid[r][col] for r in range(9) if grid[r][col] != 0]
    takenNums = [n for n in grid[row] if n != 0] # first initialise with all numbers in the cell's row
    for n in colNums:
        if n not in takenNums: takenNums.append(n) # add all non-duplicates from the cell's column

    boxStartR = row - (row % 3)
    boxStartC = col - (col % 3) # row and col are 0-indexed, so these give the (0-indexed) coordinates of the 3x3 box's top left cell
    for boxR in range(boxStartR, boxStartR + 3):
        if boxR == row: continue # already checked the cell's row
        for boxC in range(boxStartC, boxStartC + 3):
            if boxC == col: continue # already checked the cell's column 
            if grid[boxR][boxC] != 0 and grid[boxR][boxC] not in takenNums: takenNums.append(grid[boxR][boxC])

    return [n for n in range(1, 10) if n not in takenNums] # return values that are not taken by other related cells (row, col, box)

# XXX XXX first 10 grids instead of 50 first, for time testing
for grid in [sudokuArr[i] for i in range(10)]: # XXX XXX first 10 grids instead of 50 first, for time testing
    cellNumbers = [[[n for n in range(1, 10)] for _ in range(9)] for _ in range(9)] # cell[r][c] for rth row, cth column cell possible values
    isSolved = True
    while not isSolved:
        isSolved = True
        for (r, c) in [(row, col) for row in range(9) for col in range(9)]: # iterates through a row left to right, then goes to the below row
            if grid[r][c] == 0:
                isSolved = False # still exists zeroes/unsolved cells
                values = getCell(grid, r, c)
                if len(values) == 1:
                    grid[r][c] = values[0]
                    # not done here