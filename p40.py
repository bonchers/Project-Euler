'''
d1 is '1'
1-9 is until 9th decimal place

d10 is '1' (1st digit of 10)
10-99 is until 189th decimal place (9 + 2(90) = 189)

d100 is '1' (1st digit of 100)
100-999 is until 2889th decimal place (9 + 2(90) + 3(900) = 2889)
'''
lennum = [] # store length of 1-digits, 2-digits, until 6-digit
for i in range(1, 7):
    lennum.append(i * 9 * (10 ** (i - 1)))

product = 1
for y in range(2, 7):
    lennum2 = lennum.copy()
    decplace = 10 ** y
    numlen = 1
    while decplace > lennum2[0]:
        decplace -= lennum2[0]
        lennum2.pop(0)
        numlen += 1
    
    d = (10 ** (numlen - 1)) + ((decplace - 1) // numlen)
    product *= int(str(d)[(decplace % numlen) - 1])
    
print(product)