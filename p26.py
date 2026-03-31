'''
Recurring fraction test:
let fraction be c/d, where c and d are integers
if c/d is non-recurring, it can be expressed as x/(10^y)
hence, we know d must have prime factors 2 and/or 5 (to be multiplicable into 10^y)
otherwise, 10^y has no other common prime factors with d and cannot express d
c/d must be simplifiable (divide both c and d) into a form where d only has prime factors 2 and/or 5

examples:
3/9 = 3/3^2, d has no prime factors 2 or 5, thus is recurring | 3/9 = 0.(3)
2/15 = 2/(3 * 5), cannot simplify (divide both c and d) such that d has only prime factors 2 and/or 5, thus recurs | 2/15 = 0.1(3)
3/15 = 3/(3 * 5), can simplify (divide both c and d) by 3 so d has only prime factor 5, does not recur | 3/15 = 0.2
'''

primes = [2]
for n in range(3, 1000, 2):
    for prime in primes:
        if n % prime == 0:
            break
        if prime > n**0.5:
            primes.append(n)
            break

import math as m
def isRecurring(numer, denom):
    frac = [numer, denom]
    factors = [[], []]

    # find prime factors of n and d
    for i in range(2):
        for prime in primes:
            if frac[i] % prime == 0:
                factors[i].append(prime)
            if prime > frac[i]:
                break
    
    if numer % denom == 0:
        return False
        # exclude cases where fraction expresses an integer, such as 9/3
    
    if 2 not in factors[1] and 5 not in factors[1] and numer % denom != 0:
        return True
        # d has neither prime factors 2 nor 5, cannot be multiplied to 10^y, n/d recurs

    for dfactor in factors[1]:
        if dfactor == 2 or dfactor == 5:
            continue
        if dfactor not in factors[0]:
            return True
            # n does not have common factor to divide with d, to remove the non-(2 or 5) factor from both, so d is inexpressible as 10^y, n/d recurs
    
    return False

'''
let n be the recursion cycle length and d be the denominator,

1/7 = 0.(142857)
recurring cycle is 6 digits
(10^6)/7 = 142857.(142857)
(10^6 - 1)/7 = 142857
for only recurring decimals, 10^n - 1 is divisible by d

let 1/d = 0.1(68),
recurring cycle is 2 digits
(10^2)/d = 16.(86)
(10^2 - 1)/d = 16.7
including non-recurring decimals, (10^n - 1)/d is non-recurring

for both cases, (10^n - 1)/d is non-recurring

Logic:
find n for a fraction 1/d where (10^n - 1)/d is non-recurring
'''

maxrecur = maxdenom = 0

for d in range(1, 1000):
    if isRecurring(1, d):
        n = 1

        while isRecurring((10**n - 1), d):
            n += 1
        
        print(f'1/{d} | recursion length: {n}')
        if n > maxrecur:
            maxrecur, maxdenom = n, d

print(f'longest recurring fraction: 1/{maxdenom} (length: {maxrecur})')