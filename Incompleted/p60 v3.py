LIMIT = 10000
primes = [2]
def isPrime(n):
    x = int(n)
    for prime in primes:
        if prime >= x ** 0.5:
            return True
        if x % prime == 0:
            return False
for n in range(3, LIMIT, 2):
    if isPrime(n):
        primes.append(n)

def choosetwo(r):
    allchoices = []
    for i in range(r - 1):
        for j in range(i + 1, r):
            allchoices.append((i, j))
    return allchoices

primeidx = [None for _ in range(primes[-1] + 1)] # primeidx[prime] will give index, opposite of primes[]
for i in range(len(primes)):
    primeidx[primes[i]] = i # f-1(f(x)) = x

pairs = [] # indexes of primes that can concatenate
for (i, j) in choosetwo(len(primes)):
    a = int(str(primes[i]) + str(primes[j]))
    b = int(str(primes[j]) + str(primes[i]))

    if a > LIMIT ** 2 or b > LIMIT ** 2:
        continue
    if isPrime(a) and isPrime(b):
        pairs.append([i, j])

allLinks = [[] for _ in primes] # nth array contains all indexes of links to nth prime
for pair in pairs:
    allLinks[pair[0]].append(pair[1])
    allLinks[pair[1]].append(pair[0])

# look for another node in 4-loop, just find node that has two distinct pathways of length 2 from base
allpaths = [[] for _ in primes]
def findConnects(baseidx, path = []):
    if path == []: links = allLinks[baseidx]
    else: links = allLinks[path[-1]]
    
    for node in links:
        allpaths[node].append(path + [node])
        for nextnode in allLinks[node]:
            if nextnode == baseidx:
                continue
            allpaths[nextnode].append(path + [node, nextnode])

    for i in range(len(allpaths)):
        pathsToNode = allpaths[i]
        if 1 not in [len(p) for p in pathsToNode]: # check if there is path of length 1
            continue
        len2paths = [p for p in pathsToNode if len(p) == 2]
        if len(len2paths) >= 2: # one diagonal (loop[0] <> loop[2]) in square graph is connected

            ### still need to check for loop[1] <> loop[3] link

            pass
        # toremove = [] # non-distinct paths, e.g. same 1st & 3rd node but different 2nd node, must be merged, i.e. remove one
        # ^^ for 5-loop, and checking for len3paths

findConnects(1)