hundand = 10
ones = [3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [6, 6, 5, 5, 5, 7, 6, 6]
teens = [6, 6, 8, 8, 7, 7, 9, 8, 8]

twodig = sum(ones) + 3 + sum(teens) # 1 - 19

for digit in tens:
    twodig += digit
    for dig in ones:
        twodig += digit + dig

threedig = 0
for digit in ones:
    threedig += digit + 7 # N hundred
    
    threedig += ((digit + hundand) * 99) + twodig

total = threedig + twodig + 11 # 1 - 999 and 1000

print(total)