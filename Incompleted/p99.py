with open('./Text Files/p99_base_exp.txt', 'r') as p99:
    p99BaseExp = p99.read()

base = []
exp = []
for baseExp in p99BaseExp.split("\n"):
    base.append(int(baseExp.split(",")[0]))
    exp.append(int(baseExp.split(",")[1]))

base = [3, 4]
exp = [5, 4]

g = 0 # greatest pair's index in base[]/exp[], ranging 0-999 (inclusive) since p99_base_exp.txt is 1000 lines long
for i in range(1, len(base)):
    if base[i] <= base[g] and exp[i] <= base[g]: continue # cannot have base & exp both equal (no duplicates i think), so as long as one is lesser, the whole exponent is lesser
    if base[i] ** (exp[i]/exp[g]) > base[g]: g = i

print(g + 1, "|", base[g], exp[g])

'''
a = 632382
b = 518061
c = 519432
d = 525806
print(a ** (b/d) > c)     ~0.06s    <<<< this formula is far more efficient
print(a ** b > c ** d)    ~1.6s
'''