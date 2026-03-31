LIMIT = 10000
primes = [2]
compodds = []

for i in range(3, LIMIT, 2):
    for prime in primes:
        if prime > i ** 0.5:
            primes.append(i)
            break
        if i % prime == 0:
            compodds.append(i)
            break

compexpressible = [False for _ in compodds]

def isPrime(x):
    for prime in primes:
        if prime > i ** 0.5:
            return True
        if i % prime == 0:
            return False

def search(item, arr):
    min, max = -1, len(arr)

    while max - min > 1:
        check = int((max + min) / 2)
        if arr[check] > item:
            max = check
        elif arr[check] < item:
            min = check
        elif arr[check] == item:
            return check
    
    return -1

for prime in primes:
    print(prime)
    sum = prime
    root = 1
    while sum < LIMIT:
        sum = prime + (2 * root * root)
        index = search(sum, compodds)
        if index != -1:
            compexpressible[index] = True
        root += 1

for i in range(1, len(compexpressible)):
    if not compexpressible[i]:
        print(compodds[i])
        break

print('end')