maxsum = 0
for a in range(1, 100):
    for b in range(1, 100):
        exp = a ** b
        digitsum = 0
        for c in str(exp):
            digitsum += int(c)
        if digitsum > maxsum:
            maxsum = digitsum

print(maxsum)