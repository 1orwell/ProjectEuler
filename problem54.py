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

def check_straight(lst_val):
    sorted_vals = sorted(lst_val)
    for i, val in enumerate(sorted_vals):
        if val == 'T':
            sorted_vals[i] = 10
        if val == 'J':
            sorted_vals[i] = 11
        if val == 'Q':
            sorted_vals[i] = 12
        if val == 'K':
            sorted_vals[i] = 13
        if val == 'A':
            sorted_vals[i] = 14
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
            return('Royal Flush')

    # Check straight flush
    if len(counter_suits) == 1:
        in_order = check_straight(lst_val)
        if in_order == True:
            return('Straight Flush')

    # Check for four of a kind.
    if 4 in vals_check:
        return('Four of a Kind')

    # Check for full house
    if 2 in vals_check and 3 in vals_check:
            return('Full House')

    # Check for flush.
    if 5 in suits_vals:
        return('Flush')

    # Check for straight.
    in_order = check_straight(lst_val)
    if in_order == True:
        return('Straight')

    # Check for three of a kind
    if 3 in vals_check:
        return('Three of a kind')

    # Check for two pairs 
    if 2 in vals_check:
        counter = 0
        for val in vals_check:
            if val == 2:
                counter += 1
        if counter == 2:
            return('Two Pairs')

    # Check for one pair 
    if 2 in vals_check:
        return('A pair')

    return('Check highest card.')
    





    
    
    return('No pattern found.')

    
(player1, player2) = translate_file('p054_poker.txt')

for i in range(1, 1001):
    print(f'The round is {i}')
    print(f'Player 1s hand is: {check(player1[i])}')
    print(f'Player 2s hand is: {check(player2[i])}')