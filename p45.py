triindex = 286
pentindex = 166
hexindex = 144

tri = lambda : (triindex * (triindex + 1)) // 2
pent = lambda : (pentindex * ((3 * pentindex) - 1)) // 2
hex = lambda : hexindex * ((2 * hexindex) - 1)

while not tri() == pent() == hex():
    if tri() < pent() or tri() < hex():
        triindex += 1
    if pent() < tri():
        pentindex += 1
    if hex() < tri():
        hexindex += 1

print(tri())