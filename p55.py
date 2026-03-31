def ispalin(x):
    for i in range(len(str(x)) // 2):
        if str(x)[i] != str(x)[-i - 1]:
            return False
    
    return True

lychnums = 9999
for n in range(1, 10000):
    test = n
    for _ in range(50):
        test += int(str(test)[::-1])
        if ispalin(test):
            lychnums -= 1
            break

print(lychnums)