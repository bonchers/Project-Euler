LIMIT = 10000000 - 1 # n < ten million

end1 = {1}
end89 = {89}

digSquares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def findChain(x, chain = set()): # returns (end, chain) where 'end' is 1 or 89, and 'chain' is a set with the numbers iterated through
    if x in end1: return (1, chain)
    elif x in end89: return (89, chain)

    next = 0
    for d in str(x):
        next += int(d)**2

    return findChain(next, chain | {x})

for n in range(1, LIMIT + 1):
    c = findChain(n)
    if c[0] == 1: end1.update(c[1])
    else: end89.update(c[1])

print(len(end89))