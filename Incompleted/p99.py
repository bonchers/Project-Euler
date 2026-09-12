with open('./Text Files/0099_base_exp.txt', 'r') as p99:
    p99BaseExp = p99.read()

base = []
exp = []
for baseExp in p99BaseExp.split("\n"):
    base.append(int(baseExp.split(",")[0]))
    exp.append(int(baseExp.split(",")[1]))

# largest base: 999665 | largest exp: 1190800
# smallest base: 334 | smallest exp: 500894
LIMIT = max(base) # 999665 is the largest value in the bases (left column in 0099_base_exp.txt)
primes = [2]
for n in range(3, LIMIT + 1, 2):
    for p in primes:
        if p > n**0.5:
            primes.append(n)
            break
        if n % p == 0: break

factordict = {} # factordict[n] returns a dictionary of |prime factor: power| pairs for the prime factors of n, e.g. n = 2^3 * 5^7 is {2: 3, 5: 7}
for n in base + exp:
    factordict[n] = {}
    for p in primes:
        if p > n: break
        if n % p == 0:
            multiple = 1
            while n % (multiple + 1) * p == 0: # stop right before the product is no longer a factor
                multiple += 1
            factordict[n][p] = multiple

#XXX XXX XXX
#   currently factors are not entirely correct, have to fix that first
#XXX XXX XXX
# logic: compare and reduce both bases into their prime factorisations, then divide both into smaller numbers, and lastly raise to the power of respective exp

print(factordict[519432], factordict[632382])
g = 0 # index of greatest base/exp pair, ranging 0-999 (inclusive)
for i in range(1, 6):
    newg = base[g]
    newi = base[i]

    for factor in factordict[base[g]].keys():
        if factor in factordict[base[i]]:
            hcf = factor ** min(factordict[base[g]][factor], factordict[base[i]][factor]) # hcf with this particular prime factor
            print(hcf)
            newg /= hcf
            newi /= hcf

    print(newg, newi)


# g = 0 # greatest pair's index in base[]/exp[], ranging 0-999 (inclusive) since p99_base_exp.txt is 1000 lines long
# for i in range(1, len(base)):
#     if base[i] <= base[g] and exp[i] <= base[g]: continue # cannot have base & exp both equal (no duplicates i think), so as long as one is lesser, the whole exponent is lesser
#     if base[i] ** (exp[i]/exp[g]) > base[g]: g = i

# print(g + 1, "|", base[g], exp[g])

'''
a = 632382
b = 518061
c = 519432
d = 525806
print(a ** (b/d) > c)     ~0.06s    <<<< this formula is far more efficient
print(a ** b > c ** d)    ~1.6s
'''