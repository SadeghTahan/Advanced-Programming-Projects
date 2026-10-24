suits=['clubs','diamonds','hearts','spades']
ranks=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
import random
rank=random.randrange(0, len(ranks))
suit=random.randrange(0, len(suits))
print(ranks[rank] + ' of ' + suits[suit])