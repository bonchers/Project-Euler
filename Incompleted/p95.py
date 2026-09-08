LIMIT = 1000000 # no element exceeding one million
# prime numbers should not be computed as they only have one proper divisor, 1, which will loop back only to itself

primes = [2]
primeset = set() # useful for quickly checking if a number is in the primes
for n in range(3, LIMIT + 1, 2):
    for p in primes:
        if n % p == 0: break
        if p > n ** 0.5:
            primes.append(n)
            primeset.add(n)
            break
[primes[i] for i in range(40)]

def divisorSum(x):
    divsum = 1
    firstFactor = -1
    for p in primes:
        if p > x * 2 or (firstFactor != -1 and p > x/firstFactor): break
        if x % p == 0:
            sum = 0
            divisor = p
            while x % divisor == 0:
                sum += divisor
                divisor *= p

            divsum += sum * divsum
            print(sum, divsum)

    print('\n')
    return divsum - x

divisorSum(284)
divisorSum(220)

# first fix divisorSum()

for n in range(4, LIMIT + 1): # 1 will loop to itself, 2 and 3 are primes, start at 4 instead
    if n in primeset: continue
    