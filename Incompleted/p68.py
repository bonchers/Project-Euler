LIMIT = 15 # 10 + 9 + 8 = 27, theoretical max
nums = {n for n in range(1, 11)} # 1-10 inclusive

def check(target, remaining, lineEnds = {}, firstLineEnds = {}, solutionPath = []):
    solutions = []

    if len(remaining) == 10:
        sortedr = sorted(remaining) # list of sorted remaining
        for a in range(len(sortedr)):
            if sortedr[a] > target: break
            for b in range(a + 1, len(sortedr)):
                if sortedr[a] + sortedr[b] > target: break
                for c in range(b + 1, len(sortedr)):
                    testLine = {sortedr[a], sortedr[b], sortedr[c]}
                    if sum(testLine) > target: break
                    if sum(testLine) == target: solutions += check(target, remaining.copy() - testLine, testLine)

        return solutions

    if len(remaining) == 1:
        head = remaining.pop() # last node, as the head of last line
        for last in lineEnds:
            for fLast in firstLineEnds:
                if head + last + fLast == target:
                    path = solutionPath.copy()
                    path.append([head, last, fLast])
                    solutions.append(path)
                    if len(solutions) == 1: print(path)
                    break # no other solutions for this head and this last, other fLast has different value/sum

        return solutions

    for last in lineEnds: # go through every possible last node // connected with next line
        if firstLineEnds == {}: # first iteration run only
            solutionPath.append(list(lineEnds)) # path remembers full details
            firstLineEnds = lineEnds.copy()
            firstLineEnds.remove(last) # only remember {a, b} from first line, to connect with last line
        
        checkedPairs = []
        for a in remaining:
            b = target - a - last
            if b in remaining and a != b and {a, b} not in checkedPairs: # a != b prevent duplicate like {5, 5}
                checkedPairs.append({a, b}) # prevent double check like 3+4 and 4+3
                solutionPath.append([a, last, b])
                solutions += check(target, remaining.copy() - {a, b}, {a, b}, firstLineEnds, solutionPath) # add line to path
                
    return solutions

# 1 + 2 + 3 = 6, theoretical min
for targetsum in range(6, LIMIT + 1):
    print(f"\nchecked target: {targetsum}")
    for s in check(targetsum, nums):
        print(s)