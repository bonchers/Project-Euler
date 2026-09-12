with open('./Text Files/0089_roman.txt', 'r') as p89:
    p89roman = p89.read().split('\n')

def valueOf(numeral):
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeralValue = 0

    for d in range(len(numeral)):
        if d < len(numeral) - 1 and value[numeral[d + 1]] > value[numeral[d]]: numeralValue -= value[numeral[d]]
        # should be v[n[d + 1]] - v[n[d]], but v[n[d + 1]] will be double counted the next loop, so simply subtract from this iteration to counterbalance
        else: numeralValue += value[numeral[d]]

    return numeralValue

def optimalLen(x):
    optimal = x // 1000 # all the 'M'/thousands numerals first
    x %= 1000 # remove the thousands+ values
    digits = [int(s) for s in str(x)] # hundreds, tens and ones digits

    for d in digits:
        if d == 1 or d == 5: optimal += 1 # I, V or equivalent in tens/hundreds place
        elif d == 4 or d == 9: optimal += 2 # IV, IX or equivalent
        elif d != 0: optimal += (d - 1) % 4 + 1
        # this specific equation above returns 2, 3, 2, 3, 4 for inputs 2, 3, 6, 7, 8 | represents roman numeral length and making this code simpler
        # if d == 0 then dont add anything

    return optimal

charsSaved = 0
for roman in p89roman:
    difference = len(roman) - optimalLen(valueOf(roman))
    charsSaved += difference # even if roman is minimal, difference should be at least 0

print(charsSaved)