LIMIT = 1000000
primes = [2]
for i in range(3, LIMIT, 2):
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

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

seqlen = 21
while seqlen <= len(primes):
    seq = [primes[i] for i in range(seqlen)]
    if sum(seq) > primes[-1]:
        break
    for n in range(seqlen, len(primes)):
        if search(sum(seq), primes) != -1:
            longprime = sum(seq)
            break
        del seq[0]
        seq.append(primes[n])
    
    seqlen += 1

print(longprime)