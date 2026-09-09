primes = [2]
for i in range(3, 100, 2):
    for prime in primes:
        if i % prime == 0:
            break
        if prime > i ** 0.5:
            primes.append(i)
            break

def simplify(a, b):
    c, d = a, b
    afactors = []
    for prime in primes:
        if a % prime == 0:
            afactors.append(prime)
    
    for factor in afactors:
        while c % factor == 0 and d % factor == 0:
            c //= factor
            d //= factor
    
    return [c, d]

fracs = [[], [], []]
for numer in range(10, 100):
    for denom in range(numer + 1, 100):        
        for i in range(4):
            ndig = str(numer)[i // 2]
            ddig = str(denom)[i % 2]
            newfrac = [int(str(numer)[(i // 2) - 1]), int(str(denom)[(i % 2) - 1])]
            if ndig == ddig and simplify(numer, denom) == simplify(newfrac[0], newfrac[1]):
                if ndig == '0':
                    continue
                fracs[0].append([numer, denom])
                fracs[1].append(simplify(numer, denom))
                fracs[2].append(newfrac)
                break

product = [1, 1]
for f in fracs[0]:
    product[0] *= f[0]
    product[1] *= f[1]
print(f'product = {product} = {simplify(product[0], product[1])}')