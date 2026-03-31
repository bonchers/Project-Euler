fact = 1

for i in range(2, 101):
    fact *= i

s = str(fact)
sum = 0

for char in s:
    sum += int(char)

print(sum)