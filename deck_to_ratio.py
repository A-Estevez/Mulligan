######
#gets a decklist as a txt from Dueling Nexus
#gets the quantites and each unique card to a list
#finds the ratio in all_ratios_decksize
#####
import pandas as pd


f = open('ryzeal_01.txt','r') # opens decklist
lines = f.readlines()
#print(lines[1][3:])
q_c = [] #quantity card, empty list to hold the decklist
for l in lines: #checks if start of line is digit, to ignore deck name, etc and if it is adds the quantity and card name to a list
    if l[0].isdigit():
        q_c.append([int(l[0]),l[3:-1]])
    elif l[0] == '-':
        break
print(q_c)

ratios_id = [0, 0, 0] # cards at 1, 2 and 3, empty list to hold the ratios of the deck
for i in q_c: #calculates the ratios of the decklist
    if i[0] == 1:
        ratios_id[0] +=1
    elif i[0] == 2:
        ratios_id[1] += 1
    elif i[0] == 3:
        ratios_id[2] +=1
print(ratios_id)

df = pd.read_csv('all_ratios_40_name.csv', index_col=None, names=['ratio_id', 'c01','c02', 'c03', 'c04','c05','c06','c07','c08','c09','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24','c25','c26','c27','c28','c30','c31','c32','c33','c34','c35','c36','c37','c38','c39','c40','c41'])
#print(df.columns)
#print(df.loc[df['ratio_id']])
#print(df.head(5))
print(df['ratio_id'])
#ratio_names = df.loc[df['ratio_id'] == ratios_id]