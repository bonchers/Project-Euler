LIMIT = 10 ** 6
primes = [2]
for i in range(3, LIMIT, 2):
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

print('primes calculated')

def findcommon(arr : list[int], commonidx : list[int], initialidx = [-1]): # sorted arr
    if initialidx == [-1]:
        initialidx = commonidx
    if len(commonidx) == 0:
        toremove = []
        for t in arr:
            uncommondig = [int(str(t)[k]) for k in range(len(str(t))) if k not in initialidx]
            for digit in uncommondig:
                if digit != uncommondig[0]: # not in family
                    toremove.append(t)
                    break
        
        for n in toremove:
            arr.remove(n)
        return [arr]

    idx = commonidx[0]
    nextidx = commonidx.copy()
    del nextidx[0]

    allset = []
    for digit in range(0, 10):
        subset = [t for t in arr if int(str(t)[idx]) == digit]
        if len(subset) > 0:
            allset += findcommon(subset, nextidx, initialidx)

    return allset

def idxcombis(n):
    combis = [[True], [False]]
    for _ in range(1, n):
        other = [s + [True] for s in combis]
        for t in combis:
            t.append(False)
        combis += other
    
    final = []
    for t in combis:
        final.append([])
        for i in range(len(t)):
            if t[i] == True:
                final[-1].append(i)
    
    return final

prevend = -1
for l in range(1, 7): # length of primes
    primeset = []
    for k in range(prevend + 1, len(primes)):
        if primes[k] >= 10 ** l:
            break
        primeset.append(primes[k])
        prevend = k
    
    foundfam = False
    for indexes in idxcombis(l):
        if indexes == []:
            continue
        families = findcommon(primeset, indexes)
        for fam in families:
            if len(fam) == 8:
                foundfam = True
                print(fam)
                break
        if foundfam:
            break
    
    if foundfam:
        break