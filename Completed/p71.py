LIMIT = 1000000 # d <= 1 000 000

primes = [2]
for n in range(3, LIMIT + 1, 2):
    for p in primes:
        if n % p == 0: break
        if p ** 2 > n:
            primes.append(n)
            break

factors = [set() for _ in range(LIMIT)] # factors[n - 1] returns prime factors of n that are not 1 (can include n itself)
for p in primes:
    multiple = 1
    while multiple * p <= LIMIT:
        factors[multiple * p - 1].add(p)
        multiple += 1

closest = (0, 1) # (numerator, denominator)
for d in range(2, LIMIT + 1):
    if d == 7: continue
    n = int(d * 3/7) # closest numerator to 3/7
    if len(factors[n - 1] & factors[d - 1]) > 0: continue # common factors present, not a reduced proper fraction OR ratio > 3/7
    if n * closest[1] > closest[0] * d: closest = (n, d)

print(closest[0])