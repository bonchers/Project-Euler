with open('./Text Files/0054_poker.txt', 'r') as p54:
    pokers = p54.read().split()

cards = [[], []]
deal = []
for i in range(len(pokers)):
    deal.append(pokers[i])

    if i % 10 == 4:
        cards[0].append(deal)
        deal = []
    elif i % 10 == 9:
        cards[1].append(deal)
        deal = []

def cardvalue(x):
    match x[0]:
        case 'T':
            return 10
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14
        case _:
            return int(x[0])

def scorename(n):
    match n:
        case 15:
            return 'One Pair'
        case 16:
            return 'Two Pairs'
        case 17:
            return 'Three of a Kind'
        case 18:
            return 'Straight'
        case 19:
            return 'Flush'
        case 20:
            return 'Full House'
        case 21:
            return 'Four of a Kind'
        case 22:
            return 'Straight Flush'
        case 23:
            return 'Royal Flush'
        case _:
            return 'High Card: {}'.format(n)

def getscores(players : list[list]):
    score = [0, 0]
    pairnos = [0, 0]

    royalflush = ['T','J','Q','K','A']
    for i in range(2):
        hand = players[i]

        # royal flush
        findcard = royalflush.copy()
        for card in hand:
            if card[0] in findcard:
                findcard.remove(card[0])
        
        if len(findcard) == 0:
            score[i] = 23 # 9 + 14
            continue
    
        # flush/straight flush
        nums = []
        for card in hand:
            nums.append(cardvalue(card))
            
        suit = hand[0][1]
        isFlush = isStraight = True
        for card in hand:
            if card[1] != suit:
                isFlush = False
                break
        for count in range(1, 5):
            if min(nums) + count not in nums:
                isStraight = False
                break

        if isFlush or isStraight:
            if isFlush and isStraight:
                score[i] = 22 # 8 + 14
                pairnos[i] = max(nums)
            elif isFlush:
                score[i] = 19 # 5 + 14
            elif isStraight:
                score[i] = 18 # 4 + 14
                pairnos[i] = max(nums)
            continue
    
        # n of a kind
        numscopy = nums.copy()
        cardcount = []
        while len(numscopy) > 0:
            value = numscopy[0]
            cardcount.append(len([card for card in numscopy if card == value]))
            if cardcount[-1] >= 3 or (cardcount[-1] == 2 and pairnos[i] == 0):
                pairnos[i] = value
            
            while value in numscopy:
                numscopy.remove(value)
        
        if max(cardcount) >= 2:
            if max(cardcount) == 4:
                score[i] = 21 # 7 + 14
            elif max(cardcount) == 3:
                if min(cardcount) == 2:
                    score[i] = 20 # 6 + 14
                else:
                    score[i] = 17 # 3 + 14
            else:
                cardcount.remove(2)
                if 2 in cardcount:
                    score[i] = 16 # 2 + 14
                else:
                    score[i] = 15 # 1 + 14
            continue
        
        sortnums = []
        while len(nums) > 0:
            sortnums.append(min(nums))
            nums.remove(min(nums))
        
        score[i] = 18 # 4 + 14
        for k in range(len(sortnums) - 1):
            if sortnums[k] + 1 != sortnums[k + 1]:
                score[i] = 0
        
        if score[i] == 0:
            score[i] = max(sortnums)

    return [score, pairnos]

p1wins = 0
for handno in range(len(cards[0])):
    [scores, pairs] = getscores([cards[0][handno], cards[1][handno]])
    if scores[0] > scores[1]:
        p1wins += 1
    elif scores[0] == scores[1]:
        if pairs[0] == pairs[1]:
            cardvalues = [[cardvalue(c) for c in cards[0][handno]], [cardvalue(c) for c in cards[1][handno]]]
            while max(cardvalues[0]) == max(cardvalues[1]):
                cardvalues[0].remove(max(cardvalues[0]))
                cardvalues[1].remove(max(cardvalues[1]))
            
            if max(cardvalues[0]) > max(cardvalues[1]):
                p1wins += 1
        else:
            if pairs[0] > pairs[1]:
                p1wins += 1

print(p1wins)