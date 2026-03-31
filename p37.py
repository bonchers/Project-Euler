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
        check = (max + min) // 2
        if arr[check] > item:
            max = check
        elif arr[check] < item:
            min = check
        else:
            return check
    
    return -1

def isTrunc(x):
    s = str(x)
    for i in range(1, len(s)):
        if binsearch(int(s[i:]), primes) == -1 or binsearch(int(s[:i]), primes) == -1:
            return False
    
    return True

sum = 0
for prime in primes:
    if prime <= 7:
        continue
    if isTrunc(prime):
        sum += prime

print(sum)