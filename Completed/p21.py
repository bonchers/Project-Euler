def d(x) -> int:
    sum = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            sum += i + (x // i)
    
    return sum

amicsums = 0
amics = []
for n in range(1, 10000):
    if d(n) < 10000 and d(d(n)) == n and n != d(n) and n not in amics:
        amicsums += n + d(n)
        amics.append(n)
        amics.append(d(n))

print(amicsums)