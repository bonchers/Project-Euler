LIMIT = 3000
pentnums = []
pentsteps = [] # difference between each 2 consecutive terms
for i in range(1, LIMIT + 1):
    pent = i * ((3 * i) - 1) // 2
    pentnums.append(pent)
    if i > 1:
        pentsteps.append(pent - pentnums[-2])

def search(item, arr : list):
    min, max = -1, len(arr)
    if len(arr) == 0:
        return 0

    while max - min > 1:
        check = (max + min) // 2
        if arr[check] == item:
            return True
        elif arr[check] > item:
            max = check
        elif arr[check] < item:
            min = check
    
    # did not return in while loop means item lies between 2 elements (max & min), insert item in max index
    return False

mindiff = pentnums[-1] + 1
for d in range(1, LIMIT): # index difference
    print(d)
    for i in range(1, LIMIT - d):
        t1, t2 = pentnums[i], pentnums[i + d]
        if t1 + t2 > pentnums[-1]:
            break
        if search(t1 + t2, pentnums) and search(t2 - t1, pentnums) and t2 - t1 < mindiff:
            mindiff = t2 - t1

    if d == LIMIT - 1:
        break

print(mindiff)

# fix bug