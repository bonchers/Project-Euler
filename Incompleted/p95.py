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

def divisorSum(x):
    divsum = 1
    firstFactor = -1 # value of -1 represents first factor is not found yet
    for p in primes:
        if p > x * 2 or (firstFactor != -1 and p > x/firstFactor): break
        if x % p == 0:
            sum = 0
            divisor = p
            while x % divisor == 0:
                sum += divisor
                divisor *= p

            divsum += sum * divsum
    return divsum - x # don't include x itself in the sum

chainLength = [0 for _ in range(LIMIT)] # chainLength[n - 1] is for n, value of -1 means it is in a chain that exceeds LIMIT or not a chain, 0 means not checked yet
chainLength[0] = 1 # at n = 1, chainLength is 1 (it loops to itself)
longestChain = []
for n in range(2, LIMIT + 1): # 1 will loop to 0, start at 2 instead
    if n % 100000 == 0: print(n)
    if n in primeset:
        chainLength[n - 1] = 1
        continue # primes will give 1 which loops to 0, skip as they are confirmed to not be longest chains

    chain = [n]
    next = divisorSum(n)
    while next not in chain: # 3 conditions for breaking loop: (1) loop found/next is in chain, (2) next exceeds LIMIT, (3) chain length of next already found
        if next > LIMIT or chainLength[next - 1] != 0: break # if next == 1, chainlength[1 - 1] is already defined as 1 (above) so this will break
        chain.append(next)
        next = divisorSum(next)

    if next > LIMIT or chainLength[next - 1] == -1:
        for item in chain:
            chainLength[item - 1] = -1 # they lead to a chain exceeding LIMIT
        continue
    
    for i in range(len(chain)):
        if chain[i] != next:
            chainLength[chain[i] - 1] = -1
        else:
            loopStart = i
            break

    thisChainLength = len(chain) - (loopStart + 1) # add 1 to change loopStart from 0-indexed to 1-indexed
    for i in range(loopStart, len(chain)):
        chainLength[chain[i] - 1] = thisChainLength

    if thisChainLength > len(longestChain): longestChain = chain[loopStart:]

print(min(longestChain))