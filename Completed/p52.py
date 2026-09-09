LIMIT = 5 * 10 ** 6

def similar(a, b):
    for n in a:
        if n not in b:
            return False
    for n in b:
        if n not in a:
            return False
        
    return True

similar([1,2,5,8,7,4], [2,5,1,7,4,8])

e = 1
for i in range(11, LIMIT):
    if i > e * 100000:
        #print(i)
        e += 1

    if sum([i % n == 0 for n in range(2, 7)]) == 0:
        continue
    
    instances = [[int(c) for c in str(i * k)] for k in range(2, 7)]
    digits = [int(c) for c in str(i)]

    isperm = True
    for instance in instances:
        if not similar(instance, digits):
            isperm = False
    
    if isperm:
        print(i)
        break