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
    previous = int(sorted_vals[0])
    for val in sorted_vals:
        print(val)
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
    if 'T' and 'J' and 'Q' and 'K' and 'A' in lst_val:
        if len(counter_suits) == 1:
            return(0)

    # Check straight flush
    if len(counter_suits) == 1:
        in_order = check_straight(lst_val)
        if in_order == True:
            return(1)

    # Check for four of a kind.
    if 4 in vals_check:
        return(2)

    # Check for full house
    if 2 in vals_check and 3 in vals_check:
            return(3)

    # Check for flush.
    if 5 in suits_vals:
        return(4)

    # Check for straight.
    in_order = check_straight(lst_val)
    if in_order == True:
        return(5)

    # Check for three of a kind
    if 3 in vals_check:
        return(6)

    # Check for two pairs 
    if 2 in vals_check:
        counter = 0
        for val in vals_check:
            if val == 2:
                counter += 1
        if counter == 2:
            return(7)

    # Check for one pair 
    if 2 in vals_check:
        return(8)

    return(9)
    
(player1, player2) = translate_file('p054_poker.txt')

wins1 = 0
wins2 = 0
draw = 0

for i in range(1, 1001):
    print(f'The round is {i}')
    hand1 = check(player1[i])
    hand2 = check(player2[i])
    if hand1 == hand2:
        #must check highest card
        print(f'Must check highest card.')
        hand1 =  return_highest(player1[i])
        hand2 =  return_highest(player2[i])
    if hand1 > hand2:
        print('Player 1 wins.')
        wins1 += 1
    elif hand2 > hand1:
        print('Player 2 wins.')
        wins2 += 1
    else:
        print('No winner.')
        draw += 1

print(f'Player 1 has won {wins1} times.')
print(f'Player 2 has won {wins2} times.')
print(f'Draws has won {draw} times.')