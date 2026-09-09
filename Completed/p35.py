LIMIT = 1000000
primes = [2]
for i in range(3, LIMIT, 2):
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

def binsearch(item, arr):
    min, max = -1, len(arr)

    while max - min > 1:
        check = (min + max) // 2
        if arr[check] > item:
            max = check
        elif arr[check] < item:
            min = check
        else:
            return check
    
    return -1

circprimes = []
for prime in primes:
    rotations = []
    if len(str(prime)) == 1:
        circprimes.append(prime)
        continue

    for i in range(1, len(str(prime))):
        rotations.append(int(str(prime)[i:] + str(prime)[:i]))
    
    isCirc = True
    for rot in rotations:
        if binsearch(rot, primes) == -1: isCirc = False

    if isCirc: circprimes.append(prime)

print(len(circprimes))