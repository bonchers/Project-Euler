LIMIT = 10**6 - 1 # n < 1 000 000

factorial = [1] # factorial[n] returns n!
for n in range(1, 10):
    factorial.append(factorial[-1] * n)

def factSum(x):
    sum = 0
    for d in str(x):
        sum += factorial[int(d)]
    return sum

selfFactorials = set()
for n in range(LIMIT + 1):
    if factSum(n) == n: selfFactorials.add(n)
# results in selfFactorials = {1, 2, 145, 40585}

def checkLoop(x): # return remaining following terms if the latest term is part of a chain (not returning self)
    if x == 169 or x == 363601 or x == 1454: return 2
    if x == 871 or x == 45361 or x == 872 or x == 45362: return 1
    if x in selfFactorials: return 0

    return -1 # is not part of ending loop nor self factorial

def chain(x, length = 1):
    if checkLoop(x) != -1: return length + checkLoop(x)

    return chain(factSum(x), length + 1)

eligibleChains = 0
for n in range(1, LIMIT + 1):
    if chain(n) == 60: eligibleChains += 1

print(eligibleChains)