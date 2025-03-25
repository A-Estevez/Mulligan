import pandas as pd
import numpy as np
import string
import itertools
#simbolos < > 

#####
#gets a csv of all possible ratios for a 40 card deck
#and transforms it into a csv of all possible ratios with unique names for each unique card
#####

df_ratios = pd.read_csv('all_ratios_40.csv',index_col=False,  names = ('a1', 'ca1', 'a2', 'ca2', 'a3', 'ca3', 'cunicas'))

#print(df_ratios)

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
#print(template)
def df_to_ratio_list(template): #defines a function to get the ratios from a row of df_ratios
    round = 0
    deck_01 = []
    while round < template.loc['ca1'] + template.loc['ca2'] + template.loc['ca3']:
        if round < template.loc['ca1']:

            deck_01.append(all_names_40[round])
            round +=1
        elif round < template.loc['ca1'] + template.loc['ca2']:
            deck_01.append(all_names_40[round])
            deck_01.append(all_names_40[round])

            round +=1

        elif round < template.loc['ca1'] + template.loc['ca2'] + template.loc['ca3']:
            deck_01.append(all_names_40[round])
            deck_01.append(all_names_40[round])
            deck_01.append(all_names_40[round])
            round +=1
    return deck_01
#print(df_to_ratio_list(template))  #test the function
all_ratios_40_name = []
for index, row in df_ratios.iterrows():
    print(df_ratios.iloc[row]['ca1'].values[0], df_ratios.iloc[row]['ca2'].values[0], df_ratios.iloc[row]['ca3'].values[0])
    all_ratios_40_name.append([df_to_ratio_list(row), [df_ratios.iloc[row]['ca1'].values[0], df_ratios.iloc[row]['ca2'].values[0], df_ratios.iloc[row]['ca3'].values[0]]])
#print(all_ratios_40_name)

np.savetxt("all_ratios_40_name.csv", all_ratios_40_name, delimiter=",", fmt='%s')


deck_nums = list(range(0,41))
cards_numbered_temp = list(itertools.chain.from_iterable(zip(deck_01, deck_nums)))



cards_numbered = list(itertools.islice(cards_numbered_temp, 2))
#print(cards_numbered)
