LIMIT = 13
largestx = 9
maxD = 5

square = [1] # square[n] returns (n+1)^2
for D in range(8, LIMIT + 1):
    if D ** 0.5 % 1 == 0: continue

    isSolved = False
    b = 0
    while not isSolved:
        if b >= len(square): square.append((len(square) + 1) ** 2)

        a = (D * square[b] + 1) ** 0.5
        if a % 1 == 0:
            if a > largestx:
                largestx = int(a)
                maxD = D
                
            isSolved = True

    print("checked:", D)

print(f'{largestx}, D value: {maxD}')
print(len(square))