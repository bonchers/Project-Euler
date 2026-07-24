LIMIT = 20
nearestInt = 2 # nearest integer to target, in this case is e
sequence = []

# sequence for e is [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, ... 1, 2k, 1]
count = 1
for i in range(LIMIT - 1):
    if i % 3 == 1:
        sequence.append(2 * count)
        count += 1
    else: sequence.append(1)


primes = [2]
def simplify(numer, denom):
    lesser = min(numer, denom)
    factors = [p for p in primes if lesser % p == 0]
    
    for n in range(primes[-1] + 1, lesser // 2 + 1):
        for p in primes:
            if n % p == 0:
                break
            if p > n ** 0.5:
                primes.append(n)
                if lesser % n == 0: factors.append(n)
                break

    for f in factors + [lesser]: # make sure to check lesser as a factor itself
        while numer % f == 0 and denom % f == 0:
            numer //= f
            denom //= f

    return (numer, denom)

numer = 1
denom = sequence[-1]
for k in range(2, len(sequence) + 1):
    # loop from end to start
    # current element is -k + 1, next element is -k
    numer += sequence[-k] * denom
    numer, denom = denom, numer # numer/denom is now a proper fraction
    (numer, denom) = simplify(numer, denom)

(numer, denom) = simplify(numer + nearestInt * denom, denom) # add with integer outside of all fractions

print(f'{numer}/{denom} = {numer/denom}')
print(f'numerator digit sum: {sum([int(d) for d in str(numer)])}')


###### still needs optimisation