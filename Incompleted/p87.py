LIMIT = 50000000 - 1 # n < 50 million

primes = [2]
lowerLimit = -1
for n in range(3, int((LIMIT + 1) ** 0.5), 2): # check odd numbers until ceil(sqrt(LIMIT)) as p**2 <= LIMIT
    for p in primes:
        if n % p == 0: break
        if p ** 2 > n: 
            primes.append(n)
            if lowerLimit == -1 and n**2 + n**3 + n**4 > LIMIT: lowerLimit = primes[-2] # primes[-1] exceeds, p = primes[-2] is the largest p**2 <= LIMIT
            break
# upperLimit is now primes[-1]

# below = 0
# for p in primes:
#     if p <= lowerLimit: below += 1
#     else: break

### expressible = below**3 # with combination of any 3 (repetition allowed) primes <= lowerLimit, x**2 + y**3 + z**4 <= LIMIT, so include all of them first
# expressible = 23^3 = 12167

square = {}
cube = {}
fourth = {}
def getPower(x, power):
    if power == 2:
        if x not in square: square[x] = x**2
        return square[x]
    elif power == 3:
        if x not in cube: cube[x] = getPower(x, 2) * x
        return cube[x]
    elif power == 4:
        if x not in fourth: fourth[x] = getPower(x, 3) * x
        return fourth[x]
    else: print("ERROR: getPower() not given a power value from 2 to 4 (inclusive)")

expressible = set()
for a in range(len(primes)):
    for b in primes:
        sum = getPower(primes[a], 2) + getPower(b, 3)
        if sum > LIMIT: break
        for c in primes:
            sum += getPower(c, 4)
            if sum > LIMIT: break
            #if a % 100 == 0: print(primes[a], b, c)
            expressible.add(sum)
print(len(expressible))

'''
planned logic from here:
find y such that p**2 + y**3 <= LIMIT, (y <= p)
then x such that p**2 + y**3 + x**4 <= LIMIT, (x <= p)
add no. of primes <= x as they are all <= above expression, and hence <= LIMIT

if reached y such that x = p is valid, then add no. of combinations.

repeat for p in 3rd exponent and p in 4th exponent
then, decrease p to the next highest prime
continue until reached lowerLimit (DO NOT CHECK LOWERLIMIT // it is already counted, so do not double count)
'''