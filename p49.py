primes = [2]
for i in range(3, 10000, 2):
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

def search(item, arr):
    min, max = -1, len(arr)

    while max - min > 1:
        check = int((max + min) / 2)
        if arr[check] > item:
            max = check
        elif arr[check] < item:
            min = check
        elif arr[check] == item:
            return [check, True]
    
    return [max, False]

def sort(arr):
    foo = arr.copy()
    for i in range(len(foo)):
        min = i
        for j in range(i + 1, len(foo)):
            if foo[j] < foo[min]:
                min = j
        if min != i:
            foo[i], foo[min] = foo[min], foo[i]
    return foo

def perms(digits : list[str], prev = ''):
    allperms = []
    if len(digits) == 1:
        return [prev + digits[0]]

    for digit in digits:
        if digit == '0':
            continue
        newdigits = digits.copy()
        newdigits.remove(digit)
        allperms += [prev + perm for perm in perms(newdigits, digit) if prev + perm not in allperms]
    
    return allperms

start, end = search(1000, primes)[0], len(primes)
allstrs = []
for i in range(start, end):
    primeperms = [int(p) for p in perms([c for c in str(primes[i])]) if search(int(p), primes)[1] == True]

    if len(primeperms) >= 3:
        sortedperms = sort(primeperms)
        #print(primes[i], sortedperms)

        for i in range(len(sortedperms) - 2):
            for j in range(i + 1, len(sortedperms) - 1):
                for k in range(j + 1, len(sortedperms)):
                    set = [sortedperms[i], sortedperms[j], sortedperms[k]]
                    if set[2] - set[1] > set[1] - set[0]:
                        break
                    if set[2] - set[1] == set[1] - set[0]:
                        masterstr = ''
                        for p in set:
                            masterstr += str(p)
                        allstrs.append(masterstr)
                        break
                
undupe = []
for seq in allstrs:
    if seq not in undupe:
        undupe.append(seq)
        print(seq)