def sol(x, y):
    z = ((x**2) + (y**2)) ** 0.5
    if z % 1 != 0:
        return -1
    return int(x + y + z)

solutions = [0 for _ in range(1001)]
for a in range(1001):
    for b in range(a, 1001):
        if sol(a, b) != -1 and sol(a, b) <= 1000:
            solutions[sol(a, b)] += 1

print([i for (i, x) in enumerate(solutions) if x == max(solutions)], f'max = {max(solutions)}')