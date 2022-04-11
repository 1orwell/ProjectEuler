from collections import Counter

def translate_file(filename):
    player1 = {}
    player2 = {}
    play = []
    with open(filename, "r") as filestream:
        for line_index, line in enumerate(filestream):
            current_line = line.split(',')
            for cards in current_line:
                current_card = cards.split(' ')
                for i, card in enumerate(current_card):
                    # Remove the \n at the end of player2's hand
                    card = card.strip('\n')
                    play.append(card)
                    if i == 4:
                        player1[line_index+1] = play
                        play = []
                    if i == 9:
                        player2[line_index+1] = play
                        play = []
    return (player1, player2)

def sort(hand):
    lst_val = []
    for card in hand:
        lst_val.append(card[0])
    for i, val in enumerate(lst_val):
        if val == 'T':
            lst_val[i] = 10
        if val == 'J':
            lst_val[i] = 11
        if val == 'Q':
            lst_val[i] = 12
        if val == 'K':
            lst_val[i] = 13
        if val == 'A':
            lst_val[i] = 14
    for i, val in enumerate(lst_val):
        lst_val[i] = int(val)
    sorted_vals = sorted(lst_val)
    return sorted_vals

def sort_no_suits(lst_val):
    lst_val = lst_val[0]
    for i, val in enumerate(lst_val):
        if val == 'T':
            lst_val[i] = 10
        if val == 'J':
            lst_val[i] = 11
        if val == 'Q':
            lst_val[i] = 12
        if val == 'K':
            lst_val[i] = 13
        if val == 'A':
            lst_val[i] = 14
    for i, val in enumerate(lst_val):
        lst_val[i] = int(val)
    sorted_vals = sorted(lst_val)
    return max(sorted_vals)

def return_highest(hand):
    sorted_val = sort(hand)
    tmp = 0
    for val in sorted_val:
        if int(val) > tmp:
            tmp = int(val)
    return(tmp)

def check_straight(hand):
    sorted_vals = sort(hand)
    in_order = True
    # must subtract 1 as adding 1 and checking at beginning of for loop
    previous = sorted_vals[0]-1
    for val in sorted_vals:
        if previous + 1 != int(val):
            in_order = False
            break
        previous = int(val)
    return in_order

def check(hand):
    lst_val = []
    lst_suits = []

    for card in hand:
        lst_val.append(card[0])
        lst_suits.append(card[1])
    counter_vals = Counter(lst_val)
    counter_suits = Counter(lst_suits)

    vals_check = counter_vals.values()
    suits_vals = counter_suits.values() 

    # Check for Royal Flush
    if all(x in lst_val for x in ['T', 'J', 'Q', 'K', 'A']):
        if len(counter_suits) == 1:
            return(0, vals_check, suits_vals)

    # Check straight flush
    if len(counter_suits) == 1:
        in_order = check_straight(lst_val)
        if in_order == True:
            return(1, counter_vals, counter_suits)

    # Check for four of a kind.
    if 4 in vals_check:
        return(2, counter_vals, counter_suits)

    # Check for full house
    if 2 in vals_check and 3 in vals_check:
        return(3, counter_vals, counter_suits)

    # Check for flush.
    if 5 in suits_vals:
        return(4, counter_vals, counter_suits) 

    # Check for straight.
    in_order = check_straight(lst_val)
    if in_order == True:
        return(5, counter_vals, counter_suits)

    # Check for three of a kind
    if 3 in vals_check:
        return(6, counter_vals, counter_suits)

    # Check for two pairs 
    if 2 in vals_check:
        counter = 0
        for val in vals_check:
            if val == 2:
                counter += 1
        if counter == 2:
            return(7, counter_vals, counter_suits)

    # Check for one pair 
    if 2 in vals_check:
        return(8, counter_vals, counter_suits)

    return(9, counter_vals, counter_suits)

wins1 = 0
wins2 = 0
draw = 0

(player1, player2) = translate_file('p054_poker.txt')
for i in range(1, 1001):
    print(f'The round is {i}')
    (hand1, vals1, suits1)  = check(player1[i])
    (hand2, vals2, suits2) = check(player2[i])
    print(f'Player 1 has hand {player1[i]}')
    print(f'The check is {hand1}')
    print(f'Player 2 has hand {player2[i]}')
    print(f'The check is {hand2}')
    if hand1 < hand2:
        print('Player 1 wins.')
        wins1 += 1
    elif hand2 < hand1:
        print('Player 2 wins.')
        wins2 += 1
    else:
        player1_highest =  return_highest(player1[i])
        player2_highest =  return_highest(player2[i])
        #must check highest card
        print(f'Must check highest card.')
        if hand1 == 9 or hand1 == 1 or hand1 == 4 or hand1 == 5: # no pattern, or both straight flush, or flush, or straight
            if player1_highest > player2_highest:
                print('Player 1 wins.')
                wins1 += 1
            if player2_highest > player1_highest:
                print('Player 2 wins.')
                wins2 += 1
        elif hand1 == 2 or hand1 == 3 or hand1 == 6 or hand1 == 8: # four of a kind for both, or three of a kind, or a pair
            highest1 = vals1.most_common(1)[0][0]
            highest1 = sort([highest1])[0]
            highest2 = vals2.most_common(1)[0][0]
            highest2 = sort([highest2])[0]
            if highest1 > highest2:
                print('Player 1 wins.')
                wins1 += 1
            if highest2 > highest1:
                print('Player 2 wins.')
                wins2 += 1
        elif hand1 == 7: # both have two pairs
            highest1 = vals1.most_common(2)
            highest1 = [x[0] for x in highest1]
            highest1 = sort_no_suits([highest1])
            highest2 = vals2.most_common(2)
            highest2 = [x[0] for x in highest2]
            highest2 = sort_no_suits([highest2])
            if highest1 > highest2:
                print('Player 1 wins.')
                wins1 += 1
            if highest2 > highest1:
                print('Player 2 wins.')
                wins2 += 1
            


print(f'Player 1 has won {wins1} times.')
print(f'Player 2 has won {wins2} times.')

'''

royal_flush = ['TS', 'JS', 'QS', 'KS', 'AS']
print(f'Should say 0, {check(royal_flush)}')
straight_flush = ['7S', '8S', 'TS', '9S', 'JS']
print(f'Should say 1, {check(straight_flush)}')
four_kind = ['7S', '7C', '7D', 'JH', '7S']
print(f'Should say 2, {check(four_kind)}')
full_house = ['7S', 'JC', '7D', 'JH', '7S']
print(f'Should say 3, {check(full_house)}')
flush = ['7S', 'JS', '1S', 'AS', 'TS']
print(f'Should say 4, {check(flush)}')
straight = ['1S', '3C', '2D', '5H', '4S']
print(f'Should say 5, {check(straight)}')
three_kind = ['1S', '3C', '1D', '1H', '4S']
print(f'Should say 6, {check(three_kind)}')
two_pairs = ['1S', '3C', '1D', '5H', '3S']
print(f'Should say 7, {check(two_pairs)}')
one_pair = ['1S', '3C', '1D', '5H', '4S']
print(f'Should say 8, {check(one_pair)}')
nothing = ['1S', '3C', '9D', '5H', '4S']
print(f'Should say 9, {check(nothing)}')

'''