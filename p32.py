'''
upper limit of factors/product identity = XX * YYY = ZZZZ
total of 9 digits
'''
panproducts = [[] for _ in range(3)]

for a in range(10000):
    for b in range(a, 10000):
        pandigits = [False] * 9
        product = a * b
        alldig = str(a) + str(b) + str(product)

        if len(alldig) < 9:
            continue
        elif len(alldig) > 9:
            break

        for digit in alldig:
            if digit == '0':
                break

            if pandigits[int(digit) - 1] == False:
                pandigits[int(digit) - 1] = True
            else:
                pandigits[int(digit) - 1] = False
                break
        
        if sum(pandigits) == 9:
            foo = [a, b, product]
            for i in range(3):
                panproducts[i].append(foo[i])
            
print([[panproducts[k][j] for k in range(3)] for j in range(len(panproducts[0]))])
for i in range(len(panproducts[0])):
    print(panproducts[0][i], end=' * ')
    print(panproducts[1][i], end=' = ')
    print(panproducts[2][i])

nondupe = []
for p in panproducts[2]:
    if p not in nondupe:
        nondupe.append(p)
print(f'{nondupe}, sum = {sum(nondupe)}')

# answer is still wrong