corners = lambda layer, prev : [prev + ((layer * 2 - 2) * k) for k in range(1, 5)]

LIMIT = 500000
primes = [2]
def isPrime(x):
    for prime in primes:
        if x % prime == 0:
            return False
        if prime > x ** 0.5:
            return True
    return False
for i in range(3, LIMIT, 2):
    if isPrime(i): primes.append(i)

currno = 1
layerno = 1
primeratio = [0, 1]
while primeratio[0] * 10 >= primeratio[1] or layerno == 1:
    c = corners(layerno + 1, currno)
    currno = c[-1]
    layerno += 1
    primeratio[1] += 4
    for n in c[:3]:
        if isPrime(n):
            primeratio[0] += 1
    
    print(c, primeratio)

print(f'layer {layerno}: {layerno * 2 - 1}')