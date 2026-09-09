with open('./Text Files/0059_cipher.txt', 'r') as p59:
    cipher = p59.read().split(',')
# ord('a') to ord('z') = 97 to 122 (inclusive)
'''a = b'T'
b = b'c'
c = b'u'
bytes([a[0] ^ b[0]^c[0]])
chr(a[0] ^ b[0] ^ c[0])
chr(bytes([a[0] ^ b[0]^c[0]])[0])

84^117^99
chr(84^117^99)
chr(117^99^84)
ord('B')

d = '3'
bytes([ord(d)])'''

solves = []
lettercount = []

for key1 in range(97, 123):
    for key2 in range(97, 123):
        for key3 in range(97, 123):
            keys = [key1, key2, key3]
            decrypted = []
            canSolution = True
            
            for i in range(len(cipher)):
                char = int(cipher[i]) ^ keys[i % len(keys)]
                if not chr(char).isprintable():
                    canSolution = False
                    break

                decrypted.append(char)
                    
            if canSolution:
                letters = 0
                for c in decrypted:
                    if 65 <= c <= 90 or 97 <= c <= 122:
                        letters += 1
                lettercount.append(letters)
                solves.append(decrypted)

# cipher rotation with most letters
bestsolve = ''
asciisum = 0
for i in range(len(solves)):
    if lettercount[i] == max(lettercount):
        for s in solves[i]:
            bestsolve += chr(s)
            asciisum += s
        break

print(f'plain text: \"{bestsolve[:150]}...\"\nASCII value sum: {asciisum}')