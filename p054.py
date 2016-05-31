from collections import Counter


def highcard(hand):
    c = sorted([rank[hand[i][0]] for i in range(5)])
    return (14**4)*c[0]+(14**3)*c[1]+(14**2)*c[2]+14*c[3] + c[4]


def onepair(hand):
    c = dict(Counter([hand[i][0] for i in range(5)]))
    pairs = 0
    high = 'NULL'
    for key in c:
        if c[key] == 2:
            pairs += 1
            if rank[key] > rank[high]:
                high = key
    return [pairs == 1, rank[high]]


def twopair(hand):
    c = dict(Counter([hand[i][0] for i in range(5)]))
    pairs = 0
    high = 'NULL'
    for key in c:
        if c[key] == 2:
            pairs += 1
            if rank[key] > rank[high]:
                high = key
    return [pairs == 2, rank[high]]


def threekind(hand):
    c = dict(Counter([hand[i][0] for i in range(5)]))
    for key in c:
        if c[key] == 3:
            return [1, rank[key]]
    return [0, 'NULL']


def straight(hand):
    vals = list(map(lambda x: rank[x], [hand[i][0] for i in range(5)]))
    m = min(vals)
    vals = set(val-m for val in vals)
    return vals == {0,1,2,3,4}


def flush(hand):
    return (hand[0][1] == hand[1][1])*(hand[1][1] == hand[2][1])*(hand[3][1] == hand[4][1])


def fullhouse(hand):
    return threekind(hand)[0]*onepair(hand)[0]


def fourkind(hand):
    c = dict(Counter([hand[i][0] for i in range(5)]))
    for key in c:
        if c[key] == 4:
            return [1, rank[key]]
    return [0, 'NULL']

def sf(hand):
    if flush(hand):
        if straight(hand):
            return 1
    return 0


def rf(hand):
    if flush(hand):
        s = set(hand[i][0] for i in range(5))
        if s == {'T', 'J', 'Q', 'K', 'A'}:
            return 1
    return 0


def winner(hand1, hand2):
    # exhaustive list
    if rf(hand1):
        return 1
    elif rf(hand2):
        return 0

    if sf(hand1):
        if sf(hand2):
            return highcard(hand1) > highcard(hand2)
        else:
            return 1
    elif sf(hand2):
        return 0

    if fourkind(hand1)[0]:
        if fourkind(hand2)[0]:
            if fourkind(hand1)[1] == fourkind(hand2)[1]:
                return highcard(hand1) > highcard(hand2)
            else:
                return fourkind(hand1)[1] > fourkind(hand2)[1]
        else:
            return 1
    elif fourkind(hand2)[0]:
        return 0

    if fullhouse(hand1):
        if fullhouse(hand2):
            if threekind(hand1)[1] == threekind(hand2)[1]:
                return highcard(hand2) > highcard(hand2)
            else:
                return threekind(hand1)[1] > threekind(hand2)[1]
        else:
            return 1
    elif fullhouse(hand2):
        return 0

    if flush(hand1):
        if flush(hand2):
            return highcard(hand1) > highcard(hand2)
        else:
            return 1
    elif flush(hand2):
        return 0

    if straight(hand1):
        if straight(hand2):
            return highcard(hand1) > highcard(hand2)
        else:
            return 1
    elif straight(hand2):
        return 0

    if threekind(hand1)[0]:
        if threekind(hand2)[0]:
            if threekind(hand1)[1] == threekind(hand2)[1]:
                return highcard(hand1) > highcard(hand2)
            else:
                return threekind(hand1)[1] > threekind(hand2)[1]
        else:
            return 1
    elif threekind(hand2)[0]:
        return 0

    if twopair(hand1)[0]:
        if twopair(hand2)[0]:
            if twopair(hand1)[1] == twopair(hand2)[1]:
                return highcard(hand1) > highcard(hand2)
            else:
                return twopair(hand1)[1] > twopair(hand2)[1]
        else:
            return 1
    elif twopair(hand2)[0]:
        return 0

    if onepair(hand1)[0]:
        if onepair(hand2)[0]:
            if onepair(hand1)[1] == onepair(hand2)[1]:
                return highcard(hand1) > highcard(hand2)
            else:
                return onepair(hand1)[1] > onepair(hand2)[1]
        else:
            return 1
    elif onepair(hand2)[0]:
        return 0

    if highcard(hand1) == highcard(hand2):
        return "tie"
    else:
        return highcard(hand1) > highcard(hand2)


rank = {'NULL': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8,
            'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

hands = open('data54.txt', 'r')

wins = 0
ties = 0

for i in range(1000):
    hand = hands.readline().split()
    hand1 = hand[0:5]
    hand2 = hand[5:10] 
    win = winner(hand1, hand2)
    if win == 'tie':
        win = 0
        ties += 1
    wins += win

print onepair(['7H', '2C', 'KC', '5S', 'KD'])
print onepair(['6H', 'AH', 'QC', '7S', 'QH'])

print wins
print ties



