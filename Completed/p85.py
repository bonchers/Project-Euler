TARGET = 2000000 # grid closest to 2 million rectangles

def countGrid(x, y): # width-height
    # count all rects with varying width but constant height at a single y value, e.g. counting all 2 unit tall rects at the top
    # then count that, at every possible height, and every possible y value for that height
    # code for that is below
    
    # horiCount = x * (x + 1) // 2 
    # for h in range(1, y + 1): # choose height from 1 to y (inclusive)
    #     total += horiCount * (y - h + 1) # change their y value, and count them | y - h + 1 is the number of y values a height h can be at
    
    # above can be simplified to:
    # total = horiCount * (sum of all (y - h + 1))  ----  (XXX)

    # all ranges I mention below are inclusive of both ends (e.g. p to q), and sum(t) represents sum of all values of t
    # h ranges from 1 to y, so y - h will be from (y - 1) to 0, or (y - y)
    # sum(y - h + 1) will be from (y - 1 + 1) to 1, or y to 1, which is the same as sum(h) (just with inverted order)
    # sum(h) = y * (y + 1) / 2 (Gaussian sum)

    # substituting into the equation at XXX,
    # total = horiCount * (sum(h))
    #       = horiCount * (y * (y + 1) // 2)
    #       = (x * (x + 1) // 2) * (y * (y + 1) // 2)

    # Hence, it is all simplified into:
    return (x * (x + 1) // 2) * (y * (y + 1) // 2)

'''
loop logic:
without loss of generality, assume x >= y (x is greater/equal)

start at y = 1
find the minimum value x where countGrid(x, y) is above TARGET
decrease x and record the closest value to TARGET
stop decreasing x when countGrid(x, y) is below TARGET
increase y by 1
repeat loop if countGrid(x, y) is still above TARGET
'''

maxX = 1
y = 1
while countGrid(maxX, y) < TARGET:
    maxX += 1

closest = 0
closestGridArea = 0
x = maxX
count = countGrid(x, y)

while count > TARGET:
    if x < y: break
    
    above = 0
    below = count
    while below > TARGET: # find the two rect counts that are closest to 2 million (for x values that are directly above or directly below)
        above = below
        x -= 1
        below = countGrid(x, y)

    for rectCount in [[above, (x - 1) * y], [below, x * y]]:
        if abs(TARGET - rectCount[0]) < abs(TARGET - closest):
            closest = rectCount[0]
            closestGridArea = rectCount[1]

    y += 1
    count = countGrid(x, y)

print(closestGridArea)