import random
import pickle

with open('deck', 'rb') as fp:
    deck = pickle.load(fp)



total_cards = 40
desired_01 = 'Mouse'
#quantity_01 = 3
desired_02 = 'Rabbit'
#quantity_02 = 3
desired_03 = 'Cat'
#quantity_03 = 3
desired_04 = 'Bystial'
#quantity_04 = 7
desired_05 = 'Sarcophagus'
#quantity_05 = 1
desired_06 = 'Campo'
#quantity_06 = 4
desired_07 = 'ht'
#quantity_07 = 14
#cards_known = quantity_01 + quantity_02 + quantity_03 + quantity_04 + quantity_05 + quantity_06 + quantity_07

#cards_not_known = total_cards - cards_known
#deck = ([desired_01] * quantity_01) + ([desired_02] * quantity_02) + [desired_03] * quantity_03 + [desired_04] * quantity_04 + [desired_05] * quantity_05 + [desired_06] * quantity_06 + [desired_07] * quantity_07 + ['nop'] * cards_not_known

print(deck)
print( len(deck) == total_cards)
def hand(deck, size):
    return random.sample(deck, size)

test_hand = hand(deck, 5)
print(test_hand)

def ArB(hand, *desired):
    return desired[0] in hand or desired[1] in hand
def AnB(hand, *desired):
    return desired[0] in hand and desired[1] in hand
#def ArZ(hand, *desired):
#    return any i in *desired in hand



count = 0
hands = []
for i in range(1000000):
    temp_hand = hand(deck, 5)
    succes = ArB(temp_hand, desired_01, desired_02) or AnB(temp_hand, desired_03, desired_04) or ArB(temp_hand, desired_04, desired_05)
    if succes:
        count += 1
        hands.append(temp_hand)
print(hands[-1])

print(count/1000000)