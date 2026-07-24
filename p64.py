import math
LIMIT = 10000
period = [] # use -1 as placeholder for perfect squares

def descent(square, initialNumer = 0, initialValue = 0, numer = 0, value = 0, depth = 0):
    nearest = int(square ** 0.5)

    # first run
    if initialValue == 0: return descent(square, initialNumer = 1, initialValue = -nearest, numer = 1, value = -nearest, depth = depth + 1)
    
    newNumer = square - value ** 2
    newNumer /= numer
    newValue = -value
    while nearest + newValue >= newNumer: newValue -= newNumer
    
    # loop completed  
    if newNumer == initialNumer and newValue == initialValue: return depth

    return descent(square, initialNumer, initialValue, newNumer, newValue, depth + 1)

for n in range(2, LIMIT + 1):
    if (n ** 0.5) % 1 == 0: continue
    
    period.append(descent(n))

odds = 0
for l in period:
    if l % 2 == 1: odds += 1
print(odds)