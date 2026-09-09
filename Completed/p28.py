'''
side length of layer n = 2n - 1
diagonal no. indexes in layer n (zero-indexing) = (side - 1), 2*(side - 1), 3*(side - 1), 4*(side - 1)
'''
# make sure function can recur 1001 times for 1001 layers
import sys
sys.setrecursionlimit(1001)

def diagsum(k, prev, limit):
    side = (2 * k) - 1
    sum = 0

    if k == 1:
        return 1 + diagsum(k + 1, 1, limit)
    if side > limit:
        return 0
    
    print(f'layer: {k}, side length: {side}')

    nums = []
    for _ in range(4):
        prev += side - 1
        sum += prev
        nums.append(prev)
    print('corners:', nums)
    
    return sum + diagsum(k + 1, prev, limit)

print('\nsum of diagonals:', diagsum(1, 0, limit = 1001))