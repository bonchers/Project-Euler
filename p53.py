def factorial(x):
    f = 1
    for g in range(2, x + 1):
        f *= g
    
    return f

above = 0

for n in range(23, 101):
    reachedMid = False
    for r in range(n - 1, 0, -1):
        comb = factorial(n) / (factorial(r) * factorial(n - r))
        if comb > 1000000:
            reachedMid = True
            above += 1
        elif reachedMid:
            break

print(above)