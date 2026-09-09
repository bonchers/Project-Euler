'''
perm. for 2 slots: 2
perm. for 3 slots: 3 for slot one * 2 per digit in next 2 slots = 6 = 2 * 3
perm. for 4 slots: 4 for slot one * 6 per digit in next 3 slots = 24 = 2 * 3 * 4
perm. for n slots: n!
perm. for 10 slots: 10!


logic: count highest n * 9! <= 1 mil, n is first digit
^^ every 9! perm. represents 9 slots' perm. for every digit in slot one

then: count highest m * 8! <= (1 mil % 9!), m is the 2nd digit
^^ counts 8! perm. for each digit in slot two, for the next 8 slots
'''
answer = []
digits = [i for i in range(10)]
countperms = 1000000

def factorial(x):
    foo = 1
    for i in range(2, x + 1):
        foo *= i
    
    return foo

for k in range(9, 0, -1): # k = 9 to 1
    # perms = k!
    perms = factorial(k)

    if countperms % perms == 0:
        digindex = countperms // perms - 1
    else:
        digindex = countperms // perms
    answer.append(digits[digindex])
    del digits[digindex]
    countperms -= digindex * perms

answer.append(digits[0])

for digit in answer:
    print(digit, end = '')