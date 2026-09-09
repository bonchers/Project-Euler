import math as m
digitLen = lambda x : int(m.log10(x)) + 1

LIMIT = 10000

# a can only be <10. if a >= 10, a^1 is at least 2 digits (greater than target), and grows by >1 digit per exponent increment
# this means expLen will never catch up to targetLen (exponent/target digit length)
satisfies = 0
for a in range(1, 10):
    for targetLen in range(digitLen(a), LIMIT):
        expLen = digitLen(a ** targetLen)
        if expLen < targetLen: break
        if expLen == targetLen:
            satisfies += 1

print(satisfies)