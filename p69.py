LIMIT = 1000000

primes = [2]
def getFactors(x): # calculate and return array of prime factors of x, excluding 1 and x
    factors = []

    for p in primes:
        if x % p == 0 and x > p: factors.append(p) # add factors from current primes[]
        if p ** 2 > x: break

    for n in range(primes[-1] + 1, x + 1):
        for p in primes:
            if n % p == 0: break
            if p ** 2 > n:
                primes.append(n)
                if x % n == 0 and n < x: factors.append(n) # add any other factors
                break

    return factors

def choices(arr, currSet = []):
    allchoices = []

    if len(arr) == 0: return []

    for i in range(len(arr)):
        newarr = arr.copy()[i + 1:]
        allchoices += choices(newarr, currSet + [arr[i]]) + [currSet + [arr[i]]]

    return allchoices

def totient(x):
    relprimes = x - 1 # start by assuming all relatively prime, from 1 to x - 1 (inclusive)
    factors = getFactors(x)

    for fset in choices(factors):
        product = 1
        for f in fset:
            product *= f

        # remove all multiples of f, as they have a common factor with x, i.e. subtract 1/f numbers below x-1 (rounded down)
        # add back double-removed/double-factor numbers, like after removing 1/2 and 1/5, 1/2*5 numbers, or multiples of 2*5, are doubled removed
        # remove triple-factor numbers, as they are double added. 1/2*5*7 numbers, or multiples of 2*5*7 must be added back
        # this is simply the union formula for overlapping sets

        if len(fset) % 2 == 1:
            relprimes -= (x - 1) // product
        elif len(fset) % 2 == 0:
            relprimes += (x - 1) // product

    return relprimes

maxTotR = 2/totient(2) # start with totient ratio n/t(n) of 2
maxn = 2
for n in range(3, LIMIT + 1):
    currTot = totient(n)
    currTotR = n/currTot
    if currTotR > maxTotR:
        maxTotR = currTotR
        maxn = n

print(maxn)