import random
from collections import defaultdict
import pickle

total_cards = 40
cartas = [('Mouse', 3, 'Maliss'), ('Nibiru', 3, 'ht'), ('Druiswurm', 3, 'Bystial'), ('Magnamuth', 1, 'Bystial'), ('Baldrake', 3, 'Bystial'), ('Cat', 2, 'Maliss'), ('Rabbit', 3, 'Maliss'), ('Ash', 3, 'ht'), ('Veiler', 3, 'ht'), ('Allure', 2, 'Banish'), ('Sarcophagus', 1, 'Banish'), ('Campo', 3, 'Campo'), ('Impermanence', 2, 'ht'), ('GWC-06', 1, 'Trampa'), ('TB-11', 1, 'Trampa'), ('MTP-07', 1, 'Trampa'), ('Terraforming', 1, 'Campo'), ('Fuwalos', 3, 'ht'), ('Dotscaper', 1, 'Summon') ]

#print( len(deck) == total_cards
for i in cartas:
    print(i[2])
deck = []
cartas_deck = []
tipos = []
count=0
for i in cartas:
    deck.extend([i[0]] * i[1])
    if [i[0]] not in cartas_deck:
        cartas_deck.extend([i[0]])
    if [i[2]] not in tipos:
        tipos.extend([i[2]])
deck.extend(['¿?'] * (total_cards - len(deck)))
print(deck)
print(len(deck))
print(cartas_deck)
print(len(cartas_deck))
print(tipos)
print(len(tipos))



with open('deck', 'wb') as fp:
    pickle.dump(deck, fp)

with open('cards', 'wb') as fp:
    pickle.dump(cartas_deck, fp)

with open('tipos', 'wb') as fp:
    pickle.dump(tipos, fp)