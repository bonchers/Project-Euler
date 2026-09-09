LIMIT = 7830457 # p = 28433 * 2^7830457 + 1
DIGITS = 10
# LIMIT = 20
# DIGITS = 5
digitsLimit = 10**DIGITS

exponent = 1
for _ in range(LIMIT):
    exponent *= 2
    if exponent >= digitsLimit: exponent %= digitsLimit

exponent = (28433 * exponent) + 1
if exponent > digitsLimit: exponent %= digitsLimit

print(exponent)