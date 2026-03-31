def nextset(remaining : list, prev, divInd = 0):
    divisors = [3, 5, 7, 11, 13, 17]

    if len(remaining) == 1:
        lastpan = int(str(prev)[-2:] + str(remaining[0]))
        if lastpan % divisors[divInd] == 0:
            return [int(str(prev) + str(remaining[0]))]
        else: return []
    
    newpans = []
    for digit in remaining:
        newremain = remaining.copy()
        newremain.remove(digit)
        if int(str(prev)[-2:] + str(digit)) % divisors[divInd] == 0:
            newpans += nextset(newremain, int(str(prev) + str(digit)), divInd + 1)
    
    return newpans

exclude = lambda blacklist : [n for n in digits if n not in blacklist]

allpans = []
digits = [n for n in range(10)]
for a in range(10):
    for b in exclude([a]):
        for c in exclude([a, b]):
            for d in [n for n in exclude([a, b, c]) if n % 2 == 0]:
                start = int(str(a) + str(b) + str(c) + str(d))
                allpans += nextset(exclude([a, b, c, d]), start)

print(sum(allpans))