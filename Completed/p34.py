factorials = [1, 1]
for i in range(2, 10):
    factorials.append(factorials[-1] * i)

def fact(x):
    return factorials[int(x)]

LIMIT = 2600000
factsum = 0
for n in range(3,  LIMIT):
    nsum = 0
    for digit in str(n):
        nsum += fact(digit)
    if nsum == n:
        factsum += n
print(factsum)