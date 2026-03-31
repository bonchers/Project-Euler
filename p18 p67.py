# Problem 18 Pyramid

pyramid = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

with open('c:\Documents\Python Files\Project Euler\p67_pyramid.txt', 'r') as p67:
    p67pyramid = p67.read()


# rows = pyramid.split('\n') #  <<<<    Problem 18
rows = p67pyramid.split('\n') #  <<<<    Problem 67


# Solution

tri = []
for row in rows:
    t = row.split()
    nexttemp = [int(e) for e in t]
    
    tri.append(nexttemp)

def expand(arr, index):
    # if len(arr) == 15 #       <<<<    Problem 18
    if len(arr) == 100: #       <<<<    Problem 67
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
print('max:', max(final))