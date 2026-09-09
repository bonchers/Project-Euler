def isPalin(x):
    s = str(x)
    ispalin = True
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            ispalin = False
    
    return ispalin

sum = 0
for n in range(1000000):
    if isPalin(n) and isPalin(int(bin(n)[2:])):
        sum += n

print(sum)