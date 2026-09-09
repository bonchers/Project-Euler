with open('./Text Files/0067_pyramid.txt', 'r') as p67:
    p67pyramid = p67.read()

rows = p67pyramid.split('\n')

tri = []
for row in rows:
    t = row.split()
    nexttemp = [int(e) for e in t]
    
    tri.append(nexttemp)

def expand(arr, index):
    if len(arr) == 100:
        return arr
    
    temp = []
    for _ in range(len(arr) + 1):
        temp.append([])
    
    newarr = []

    for i in range(len(arr)):
        temp[i + 1].append(arr[i] + tri[index + 1][i + 1])
        temp[i].append(arr[i] + tri[index + 1][i])
    
    for z in temp:
        high = 0
        for n in z:
            if n > high:
                high = n
        
        newarr.append(high)
    
    return expand(newarr, index + 1)

final = expand(tri[0], 0)
print(max(final))