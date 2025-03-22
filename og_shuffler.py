import random
import time
import numpy as np


t = time.process_time()
#do some stuff





deck_len = 40
deck = np.array(range(deck_len))
#print(deck)
itrs = 1000000					
decks_sh = []




for i in range(itrs):
    deck_sh = np.random.choice(deck, size=len(deck), replace=False)
    decks_sh.append(deck_sh)

#print(decks_sh)
np.savetxt("all_decks_40.csv", decks_sh, delimiter=",", fmt='%s')
#https://stackoverflow.com/questions/20033458/python-rename-files-reading-names-from-csv-file
elapsed_time = time.process_time() - t
print(elapsed_time)