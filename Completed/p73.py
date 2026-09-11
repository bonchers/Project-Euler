LIMIT = 12000 # d <= 12000
factors = [[] for _ in range(LIMIT)] # factors[n - 1] returns prime factors of n except 1 and n

primes = [2]
for n in range(3, int(LIMIT/2) + 1, 2):
    for p in primes:
        if p > n ** 0.5:
            primes.append(n)
            break
        if n % p == 0: break

for p in primes:
    multiple = 2 * p
    while multiple <= LIMIT:
        factors[multiple - 1].append(p)
        multiple += p

between = 0 # no. of fractions that lie between 1/3 and 1/2
for d in range(2, LIMIT + 1):
    for n in range(int(d/3) + 1, int((d + 1)/2)): # start at n/d right after 1/3 | end at < 1/2
        # logic for start: int(d/3) = floor(d/3), int(d/3) + 1 gives n, for n/d right above 1/3
        # logic for end: int((d + 1)/2) gives n/d right above exact 1/2 if d is odd, or exact 1/2 if d is even, either way it stops before n/d = 1/2
        isReduced = True
        for nfactor in factors[n - 1]:
            if nfactor in factors[d - 1]:
                isReduced = False # if have common prime factors, fraction is not reduced
                break

        if isReduced: between += 1

print(between)