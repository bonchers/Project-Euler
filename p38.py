def isPan(x):
    s = str(x)
    multi = 2
    while len(s) < 9:
        s += str(x * multi)
        multi += 1
        if len(s) > 9:
            return 0
            
    digits = [False for _ in range(9)]
    for digit in s:
        if digits[int(digit) - 1] == True or digit == '0':
            return 0
        digits[int(digit) - 1] = True
    
    if sum(digits) == 9:
        return int(s)

maxpan = 0
for i in range(10000):
    if isPan(i) > maxpan:
        maxpan = isPan(i)

print(maxpan)