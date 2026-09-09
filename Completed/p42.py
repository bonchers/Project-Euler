with open('./Text Files/0042_words.txt', 'r') as p42:
    words = p42.read()
wordlist = words.strip('\"').split('\",\"') #  ","

trinums = []
for i in range(1, 1001):
    trinums.append(i * (i + 1) // 2)

triwords = 0
for word in wordlist:
    value = 0
    for char in word:
        value += ord(char) - 64
    for num in trinums:
        if num < value:
            continue
        elif value >= num:
            if value == num:
                triwords += 1
            break

print(triwords)