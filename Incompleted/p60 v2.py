LIMIT = 100000
primes = [2]
def isPrime(x):
    if x <= 1:
        return False
    for prime in primes:
        if x % prime == 0:
            return False
        if prime > x ** 0.5:
            return True
for i in range(3, LIMIT, 2):
    if isPrime(i): primes.append(i)
'''
test = [311, 113, 173, 317, 323, 233, 1117, 1711, 1123, 2311, 1723, 2317]
for x in test:
    print(x, isPrime(x))
'''
def containprimes(n):
    contain = []
    for l in range(1, len(str(n))):
        front, back = int(str(n)[:l]), int(str(n)[l:])
        if isPrime(front) and isPrime(back) and front != back:
            contain.append([front, back])

    return contain

concatpairs = []
for prime in primes:
    for pair in containprimes(prime):
        if pair not in concatpairs:
            concatpairs.append(pair)

primeidx = {} # primeidx[p] returns unique index of prime p in a list
primelist = [] # reverse function of above, primelist[i] returns prime of index i
twowaypairs = []
while concatpairs != []:
    check = concatpairs[0][::-1]
    try:
        concatpairs.remove(check)
    except:
        pass
    else:
        twowaypairs.append(concatpairs[0])
        for p in concatpairs[0]:
            if p not in primelist:
                primelist.append(p)
    
    del concatpairs[0]

for (i, p) in enumerate(primelist):
    primeidx.update({p : i}) # {prime : index of prime}

def selsort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

links = [[] for _ in primeidx]  # prime index's connections to other prime indexes, contains only index values
for pair in twowaypairs:    # assigns primes from their index in primeidx to position in links
    links[primeidx[pair[0]]].append(primeidx[pair[1]])
    links[primeidx[pair[1]]].append(primeidx[pair[0]])
for l in links: selsort(l)


def findmutuals(idxs, masterarr):
    mutuals = []
    connects = []
    for i in idxs:
        connects.append(masterarr[i].copy())
    
    lastvalue = connects[0][0]
    while sum([len(x) == 0 for x in connects]) == 0:
        isSame = True
        for list in connects:
            while list[0] < lastvalue:
                del list[0]
                isSame = False
                if len(list) == 0: break
            
            if len(list) == 0: break
            lastvalue = list[0]
        
        if isSame:
            mutuals.append(connects[0][0])
            for list in connects:
                del list[0]
    
    return mutuals

def getloops(idxs, masterarr, targetsize):
    allLoops = []

    if len(idxs) == targetsize:
        return idxs

    for m in findmutuals(idxs, masterarr):
        nextidxs = idxs.copy() + [m]
        nextiter = getloops(nextidxs, masterarr, targetsize)
        if len(nextiter) > 0: allLoops += [nextiter]
    
    return allLoops

for idxsum in range(1, len(links) * 2 - 3):
    breakout = False
    for a in range(idxsum // 2):
        b = idxsum - a
        if b >= len(links): continue

        nodeloop = [a, b]
        '''for loops in getloops(nodeloop, links, 4):
            for l in loops:
                print(sum(l), l)'''
        if len(getloops(nodeloop, links, 4)) > 0:
            loop = getloops(nodeloop, links, 4)[0][0]
            print(loop, [primelist[i] for i in loop])
            breakout = True
            break
    
    if breakout: break

    #gives wrong answer, testcase at line 1-16