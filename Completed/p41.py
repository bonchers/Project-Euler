def combinations(digits : list, prev):
    if len(digits) == 1:
        return [int(str(prev) + str(digits[0]))]
    
    combis = []
    for digit in digits:
        unused = digits.copy()
        unused.remove(digit)
        combis += combinations(unused, int(str(prev) + str(digit)))

    return combis

def binsearch(item, arr):
    min, max = -1, len(arr)

    while max - min > 1:
        check = (max + min) // 2
        if arr[check] > item:
            max = check
        if arr[check] < item:
            min = check
        elif arr[check] == item:
            return check
    
    return -1

primes = [2]
e = 1
for i in range(3, int(1000000000 ** 0.5 + 1), 2): # 10^9 is max, (10^9)^0.5 is max prime factor to be checked
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

maxpanprime = 1
for n in range(2, 10):
    pandigits = combinations([i for i in range(1, n + 1)], 0)
    for pan in pandigits:
        for prime in primes:
            if pan % prime == 0:
                break
            if prime > pan ** 0.5:
                if pan > maxpanprime:
                    maxpanprime = pan
                break

print(maxpanprime)