import math
LIMIT = 10000
TARGETPERMS = 5

digitdb = {} # stores in "digits":[roots], digits is a string counting each digit, eg. "1000010000" for one '0' and one '5'

for x in range(100, LIMIT + 1):
    cube = x ** 3

    digits = [0 for _ in range(10)]
    for d in str(cube): digits[int(d)] = int(digits[int(d)]) + 1

    dstr = ""
    for c in digits: dstr += str(c)

    try:
        digitdb[dstr].append(x)
    except:
        digitdb[dstr] = [x]

satisfies = []
for nums in digitdb.values():
    if len(nums) == TARGETPERMS: satisfies += nums

print(min(satisfies) ** 3)