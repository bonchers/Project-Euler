import math as m
LIMIT = 100000
primesetsize = 4

primes = [2]
def isPrime(x):
    for prime in primes:
        if x % prime == 0:
            return False
        if prime > x ** 0.5:
            return True
for i in range(3, LIMIT, 2):
    if isPrime(i):
        primes.append(i)

def binsearch(item, arr):
    max, min = len(arr), -1

    while max - min > 1:
        check = int((max + min)/2)

        if arr[check] > item:
            max = check
        elif arr[check] < item:
            min = check
        else:
            return check
    
    return -1

# integer value of n ln(n), where n ln(n) is the estimation of the nth prime
weight = lambda x: [int(n * m.log(n)) for n in x] if type(x) == list else int(x * m.log(x))
unweight = lambda z: [m.ceil()] #finish this

def sumcombis(s, setsize, prev = [], setidx = 0): # s is the sum, prev is list of (1-based) indexes of primes
    if sum(weight(prev)) > s: return []
    if setidx == setsize - 1:
        if s - sum(weight(prev)) > weight(max(prev)):
            return [prev + [(s - sum(prev))]]
        else: return []

    allsets = []
    maxofprev = -1 if prev == [] else max(prev)
    for i in range(maxofprev + 1, s - sum(prev) + 1):
        currset = prev.copy()
        currset.append(i)
        allsets += sumcombis(s, setsize, currset, setidx + 1)
    
    return allsets

# assign weights to primes linearly, i.e. 0, 1, 2, ..., and iterate through increasing sums of weights of primes
# not accurate as primes are not linearly distributed (weight = x), greater accuracy would use prime estimation (weight = x ln(x))
combine = lambda a, b: int(str(a) + str(b))
for idxsum in range(110, len(primes)):
    for set in sumcombis(idxsum, primesetsize):
        primeset = [primes[k] for k in set]
        isSolution = True
        for i in range(len(primeset) - 1):
            for j in range(i + 1, len(primeset)):
                if not (isPrime(combine(primeset[i], primeset[j])) and isPrime(combine(primeset[j], primeset[i]))):
                    isSolution = False
                    break
        
        #print(sum(primeset), idxsum)
        if isSolution:
            print(sum(primeset), primeset)
            break
    
    if isSolution: break
    #print(idxsum)

# finish line 33