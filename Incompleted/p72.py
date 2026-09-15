LIMIT = 1000000 # d <= 1 000 000

reducedProper = (LIMIT * (LIMIT + 1)) // 2
#reducedProper -= LIMIT

primes = [2]
for n in range(3, LIMIT + 1, 2):
    for p in primes:
        if p > n**0.5:
            primes.append(n)
            break
        if n % p == 0: break

primeFactors = {}
for p in primes:
    multiple = 2 * p
    while multiple <= LIMIT:
        if multiple not in primeFactors: primeFactors[multiple] = []
        primeFactors[multiple].append(p)
        multiple += p

def factorUnion(remaining, value = 1, depth = 1):
    allUnions = [[], []] # even, odd

    for r in range(len(remaining)):
        allUnions[depth % 2].append(value * remaining[r])
        next = factorUnion(remaining[r + 1:], value * remaining[r], depth + 1)
        allUnions[0] += next[0]
        allUnions[1] += next[1]
    
    return allUnions

for d in range(1, LIMIT + 1):
    if d not in primeFactors: continue

    [even, odd] = factorUnion(primeFactors[d])
    for f in odd:
        reducedProper -= (d - 1) // f
    for f in even:
        reducedProper += (d - 1) // f

print(reducedProper)