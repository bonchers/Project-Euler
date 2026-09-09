limit = 28124

divsums = [0 for _ in range(limit)]
for i in range(1, limit):
    for j in range(i * 2, limit, i):
        divsums[j] += i
abunnums = [n for (n, x) in enumerate(divsums) if x > n]
# ^^ above copied from solution

canSum = [False for _ in range(limit)]
for i in range(0, len(abunnums)):
    for j in range(i, len(abunnums)):
        if abunnums[i] + abunnums[j] >= limit:
            break
        canSum[abunnums[i] + abunnums[j]] = True

print(sum([i for (i, x) in enumerate(canSum) if x == False]))