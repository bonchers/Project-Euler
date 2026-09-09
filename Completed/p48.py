limiter = 10 ** 10 # any number % 10^10 = last 10 digits
sum = 0
for n in range(1, 1001):
    sum += (n ** n) % limiter
    sum %= limiter

print(sum)