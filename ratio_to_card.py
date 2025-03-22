import pandas as pd
import numpy as np
import string
import itertools
#simbolos < > 

df_ratios = pd.read_csv('all_ratios_40.csv',index_col=False,  names = ('a1', 'ca1', 'a2', 'ca2', 'a3', 'ca3', 'cunicas'))
df_decks = pd.read_csv('all_decks_40.csv', header = None)

#print(df_ratios)
#print(df_decks.columns)

alfabet = list(string.ascii_lowercase)
#print(alfabet)

a = [alfabet, alfabet]
#print(a)
temp_alfbt_dupt = list(itertools.product(*a))
alfbt_dupt = []
for i in temp_alfbt_dupt:
    aa = i[0] + i[1]
    alfbt_dupt.append(aa)
#print(alfbt_dupt)
all_names_40 = alfbt_dupt[0:40]
#print(all_names_40)

deck_01 = []
round = 0
template = df_ratios.iloc[0]
print(template)
while round < template.loc['ca2']:
    deck_01.append(all_names_40[round])
    deck_01.append(all_names_40[round])
    round +=1
else:
    while round < template.loc['ca2'] + template.loc['ca3']:
        deck_01.append(all_names_40[round])
        deck_01.append(all_names_40[round])
        deck_01.append(all_names_40[round])
        round +=1

print(deck_01)
print(len(deck_01))
print(len(np.unique(deck_01)))
print(template.loc['cunicas'])
print(len(np.unique(deck_01)) == template.loc['cunicas'])

deck_nums = list(range(0,41))
cards_numbered_temp = list(itertools.chain.from_iterable(zip(deck_01, deck_nums)))



cards_numbered = list(itertools.islice(cards_numbered_temp, 2))
print(cards_numbered)
