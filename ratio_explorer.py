import numpy as np
import itertools

deck_len = 40
deck = list(range(deck_len + 1))
#print(deck)

poss_rts = [1, 2, 3]


a = [[1],deck, [2],deck, [3], deck]
#print(a)
combs = list(itertools.product(*a))
print(combs[0][1])

consistent_rts = []
for i in combs:
    if i[0]*i[1] + i[2]*i[3] + i[4]*i[5] == deck_len:
        unics = i[1] + i[3] + i[5]
        i = list(i)
        i.append(unics)
        consistent_rts.append(i)
#print(consistent_rts)
np.savetxt("all_ratios_40.csv", consistent_rts, delimiter=",", fmt='%s')