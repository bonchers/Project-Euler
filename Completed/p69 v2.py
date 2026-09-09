LIMIT = 1000000 # n <= 1 000 000

primes = [2]
for n in range(3, int(LIMIT/2 + 1), 2):
    for p in primes:
        if p**2 > n:
            primes.append(n)
            break
        if n % p == 0: break

factorlist = [[] for _ in range(LIMIT)] # factorlist[n - 1] returns prime factors of n, excluding 1 and n
for p in primes:
    multiple = 2 * p # start from 2p as prime factors of n will not include itself, i.e. factorlist[p - 1] should not include p
    while multiple < LIMIT:
        factorlist[multiple - 1].append(p)
        multiple += p
# why exclude 1 and x? 1 is not considered anyway, it is always relatively prime, not computed in totient()
# in the case of x, totient() computes and removes any multiples of a factor, f, or removes 1/f numbers below x (rounded down)
# numbers below x do not contain a multiple of x (they are less than x itself), so it is not computed anyway

def choices(arr, currSet = []):
    allchoices = []

    if len(arr) == 0: return []

    for i in range(len(arr)):
        newarr = arr.copy()[i + 1:]
        allchoices += choices(newarr, currSet + [arr[i]]) + [currSet + [arr[i]]]

    return allchoices

def totient(x):
    relprimes = x - 1 # start by assuming all relatively prime, from 1 to x - 1 (inclusive)

    for fset in choices(factorlist[x - 1]):
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
    currTotR = n/totient(n)
    if currTotR > maxTotR:
        maxTotR = currTotR
        maxn = n

print(maxn)