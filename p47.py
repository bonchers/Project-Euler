LIMIT = 250000
primes = [2]
for i in range(3, LIMIT, 2):
    for prime in primes:
        if prime > i ** 0.5:
            primes.append(i)
            break
        if i % prime == 0:
            break

def factors(x):
    list = []
    for prime in primes:
        if prime > x:
            break
        if x % prime == 0:
            list.append(prime)
            while x % prime == 0:
                x //= prime
    
    return list

nums = [1, 2, 3, 4]
for i in range(LIMIT - 3):
    allhas4 = True
    for num in nums:
        if len(factors(num)) != 4:
            allhas4 = False
            break
    
    if allhas4:
        print(nums[0])
        break

    nums.remove(nums[0])
    nums.append(nums[-1] + 1)