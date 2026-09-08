def n(c : str):
    return ord(c) - 64

def selsort(arr : list):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

def selsorttwo(arr : list, val : list):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if val[j] < val[min]:
                min = j

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            val[i], val[min] = val[min], val[i]

with open('./Text Files/0022_names.txt', 'r') as p22:
    nameslist = p22.read()

namestemp = nameslist.split(',')
names = []
for name in namestemp:
    names.append(name.strip('\"'))

sortednames = []
def sep(namlist: list, check: int = 0):
    if len(namlist) <= 1:
        if len(namlist) == 1:
            sortednames.append(namlist[0])
        return
    if check == 11:
        for name in namlist:
            sortednames.append(name)
        return
    
    separate = [[] for _ in range(27)]

    for name in namlist:
        if len(name) - 1 >= check:
            separate[n(name[check])].append(name)
        else:
            separate[0].append(name)
    
    # remove empty arrays in separate
    for item in separate:
        if item == []:
            separate.remove(item)

    for item in separate:
        sep(item, check + 1)

sep(names)

scores = []
for i in range(len(sortednames)):
    scores.append(0)
    for char in sortednames[i]:
        scores[i] += n(char)

    scores[i] *= i + 1

# test for names in index range
'''for i in range(10, 25):
    print(sortednames[i], scores[i])'''

scoresum = 0
for score in scores:
    scoresum += score

print(scoresum)