'''
fracpart = frac - 1
= a/b - b/b
= (a - b)/b
nextfracpart = 1/(2 + fracpart)
= 1/(2b/b + (a - b)/b)
= 1/((a + b)/b)
= b/(a + b)

nextfrac = 1 + b/(a + b)
= (a + b + b)/(a + b)
= (a + 2b)/(a + b)
'''
nextfrac = lambda a, b : [b + (a + b), a + b]

frac = [3, 2]
numermore = 0
for _ in range(1000):
    if len(str(frac[0])) > len(str(frac[1])):
        numermore += 1
    frac = nextfrac(frac[0], frac[1])

print(numermore)