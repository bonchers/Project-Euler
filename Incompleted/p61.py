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

'''for O(n^10)'''
# numsInBase = [[] for _ in range(9)] # numsInBase[b] returns all numbers of figurate base b
# for b in range(3, 9):
#     n = 5
#     while figurate(b, n) < 10000:
#         f = figurate(b, n)
#         if f >= 1000:
#             numsInBase[b].append(figurate(b, n))
#         n += 1

'''better solution'''
basesInNum = [[] for _ in range(10000)] # basesInNum[n] returns all figurate bases of n
fignums = [] # all 4-digit figurate numbers | length: 299
for b in range(3, 9):
    n = 5
    while figurate(b, n) < 10000:
        f = figurate(b, n)
        if f >= 1000:
            basesInNum[f].append(b)
            if f not in fignums: fignums.append(f)
        n += 1

digitInOrder = lambda a, b : a >= (b % 100) * 100 and a < ((b % 100) + 1) * 100 # last 2 digits = next first 2 digits
# alldigInOrder = lambda a : [x for x in range((a % 100) * 100, ((a % 100) + 1) * 100)]

linksof = [[] for _ in range(10000)] # next nums with correct digit order
for n in fignums:
    for other in fignums:
        if other == n: continue
        if digitInOrder(n, other): linksof[n].append(other)

def findnext(n, base, prev = []):
    solution = []
    nextbase = base + 1
    if nextbase == 9: nextbase == 3
    if prev == []: prev.append(n)

    for next in linksof[n]:
        if nextbase in basesInNum[next]:
            if len(prev) == 6 and next == prev[0]:
                return prev
            if next in prev: continue

            solution += findnext(next, nextbase, prev + [next])
    
    return solution

'''fix down here'''
for n in fignums:
    for b in basesInNum[n]:
        if findnext(n, b) != []:
            print(findnext(n, b))
            break

'''not very quick solution O(n^10) ;-;'''
# def descend(nums = [], base = 3):
#     solution = []
#     nextbase = base + 1
#     if nextbase == 9: nextbase = 3

#     for n in numsInBase[base]:
#         if len(nums) == 0: solution += descend([n], nextbase)
        
#         if not digitInOrder(nums[-1], n): continue
#         if nextbase == 3 and n == nums[0]:
#             return nums
#         solution += descend(nums + [n], nextbase)
    
#     return solution

