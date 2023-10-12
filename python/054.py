T, J, Q, K, A = range(10, 15) # Ten, Jack, Queen, King, Ace
high, pair, twoP, toaK, stra, flus, full, foaK, stFl = range(100, 109)

def classify(hand):
    """
    Input: a poker hand in the format: [8C,TS,KC,9H,4S]

    Output: a list [Rank, Values] summarizing the hand
    """
    values, suits = {}, {}

    for card in hand:
        try:
            val = int(card[0]) # 1, 2, ..., 8, 9
        except ValueError: # 'T', 'J', 'Q', 'K', 'A'
            if card[0] == 'T':
                val = T
            elif card[0] == 'J':
                val = J
            elif card[0] == 'Q':
                val = Q
            elif card[0] == 'K':
                val = K
            else:
                val = A

        values[val] = values.get(val, 0) + 1

        # ONLY FIND SUIT IF THERE ARE 5 DISTINCT VALUES
        suit = card[1]
        suits[suit] = suits.get(suit, 0) + 1

    by_value = {}

    # sort by dict_keys (card values: A, K, ..., 2, 1) (highest-lowest)
    for val in sorted(values, reverse = True):
        by_value[val] = values[val]

    # Sort by dict_values (count of each card) (highest-lowest))
    by_count = {}
    for val in sorted(by_value, key=by_value.get, reverse=True):
        by_count[val] = by_value[val]

    values = list(by_count.keys())
    counts = list(by_count.values())

    if len(by_count) == 5: # no pairs, 3/4 of a kind
        if len(suits) == 1: # Flush
            if (values[0] - values[4]) == 4: # Straight
                return stFl, values[0] # straight flush, max
            elif values == [A,5,4,3,2]:
                return stFl, 5 # straight flush, max=5
            else:
                return flus, values
        elif (values[0] - values[4]) == 4: # Straight
            return stra, values[0] # straight, max
        elif values == [A,5,4,3,2]:
            return stra, 5 # straight, max=5

        else:
            return high, values # high card

    elif len(by_count) == 4:
        if counts[0] == 2:
            return pair, values # one pair
        else:
            return "Error", values

    elif len(by_count) == 3:
        if counts[0] == 2:
            return twoP, values # two pairs
        elif counts[0] == 3:
            return toaK, values # three of a kind
        else:
            return "Error", values

    elif len(by_count) == 2:
        if counts[0] == 3:
            return full, values # full house
        elif counts[0] == 4:
            return foaK, values # four of a kind
        else:
            return "Error", values


with open('../data/054.txt', 'r') as f:
    #data = [[num for num in line.split()] for line in f]
    W, L, D = 0, 0, 0
    for line in f:
        game = [card for card in line.split()]
        p1, p2 = game[:5], game[5:]
        h1, h2 = classify(p1), classify(p2)

        if h1 > h2:
            W += 1
        elif h1 < h2:
            L += 1
        else:
            D += 1

print('W: {}, L: {}, D: {}'.format(W,L,D))
