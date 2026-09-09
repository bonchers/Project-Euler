''' n^2 + an + b, where |a| < 1000 and |b| <= 1000
-1000 < a < 1000
-1000 <= b <= 1000

let f(n) = n^2 + an + b
= n(n + a) + b

b cannot equal to n for f(n) to be a prime (otherwise f(n) = n(n + a) + n = n(n + a + 1))
b > all consecutive values of n

when n = 0, f(n) = 0(0 + a) + b = b
b must be a positive prime (for when n = 0)


'''
def binsearch(val, arr : list):
    min, max = 0, len(arr)
    
    while max - min > 1:
        check = (max + min) // 2
        if arr[check] > val:
            max = check
        elif arr[check] < val:
            min = check
        else:
            return check
    
    return -1

primes = [2]
for i in range(3, 50001, 2):
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

def primeLimit(j, k, max = 250):
    for n in range(max):
        if binsearch((n * (n + j)) + k, primes) == -1:
            return n - 1

maxlimit = 0
coeffs = []
for a in range(-999, 1000):
    for b in primes:
        if b > 1000:
            break
        limit = primeLimit(a, b)
        if limit > maxlimit:
            maxlimit = limit
            coeffs = [a, b]

print(f'a * b = {coeffs[0]} * {coeffs[1]}\n= {coeffs[0] * coeffs[1]}')