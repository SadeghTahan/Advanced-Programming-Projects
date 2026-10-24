import random
suits=['clubs','diamonds','hearts','spades']
ranks=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
deck=[]
for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)
n = len(deck)
for i in range(n):
    r = random.randrange(0, i+1)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp
for cards in deck:
    print(cards)