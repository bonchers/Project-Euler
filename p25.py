import math as m
thousanddig = 10**999

def reduce(layer : list[int]):
    while len(layer) > 2:
        layer[1] += layer[0]
        layer[2] += layer[0]
        del layer[0]

fibos = [2]
for i in range(6000): # ith iteration is for (i + 4)th Fibo. no.
    nextfibo = [1, 1]
    for _ in range(i + 1):
        nextfibo.append(0)
    
    reduce(nextfibo)
    fibos.append(sum(nextfibo))

max, min = 6000, 2900
while max - min > 1:
    check = (max + min) // 2
    if fibos[check] > thousanddig:
        max = check
    elif fibos[check] < thousanddig:
        min = check
    else:
        print(check + 3)
        break

print('index: {} | log: {}'.format(max + 3, m.log10(fibos[max])))