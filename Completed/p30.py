limit = 1000000 # increase to higher than greatest valid number
sum = 0
for i in range(2, limit + 1):
    digsum = 0
    for digit in str(i):
        digsum += int(digit) ** 5
    if digsum == i:
        sum += i
        print(i)

print(sum)