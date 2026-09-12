def figurate(base, n):
    if base == 3:
        return n * (n + 1) // 2
    if base == 4:
        return n ** 2
    if base == 5:
        return n * (3*n - 1) // 2
    if base == 6:
        return n * (2*n - 1)
    if base == 7:
        return n * (5*n - 3) // 2
    if base == 8:
        return n * (3*n - 2)

figurates = {3:[], 4:[], 5:[], 6:[], 7:[], 8:[]} # figurates[n] gives array of figurates base n
for base in range(3, 9):
    i = 1
    while figurate(base, i) < 1000:
        i += 1

    fig = figurate(base, i)
    while fig < 10000:
        figurates[base].append(fig)
        i += 1
        fig = figurate(base, i) # since i is increasing, fig is also increasing, so arrays in figurates will be by nature, sorted (least to most)

def isCyclic(a, b):
    endA = int(str(a)[-2:])
    startB = int(str(b)[:2])
    return int(endA == startB) # 0 means False // not cyclic, 1 means True // is cyclic

def search(arr, missingFigs): # missingFigs is a set, of figurate bases (3-8) which are not yet in arr
    solution = []
    if len(missingFigs) == 0:
        if isCyclic(arr[-1], arr[0]): return arr
        return []

    for base in missingFigs:
        for fig in figurates[base]:
            if isCyclic(arr[-1], fig) == 0: continue
            if isCyclic(arr[-1], fig) == -1:
                print(arr)
                return []
            else: solution += search(arr + [fig], missingFigs - {base})

    return solution

for start in figurates[3]:
    result = search([start], {i for i in range(4, 9)})
    if len(result) > 0:
        print(sum(result))
        break