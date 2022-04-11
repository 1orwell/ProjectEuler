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

def check(hand):
    lst_val = []
    lst_suits = []
    for card in hand:
        lst_val.append(card[0])
        lst_suits.append(card[1])
    counter_suits = Counter(lst_suits)
    if 'T' and 'J' and 'Q' and 'K' and 'A' in lst_val:
        if len(counter_suits) == 1:
            return('Royal Flush')
    

(player1, player2) = translate_file('p054_poker.txt')

for i in range(1, 1001):
    print(f'The round is {i}')
    print(f'Player 1s hand is: {player1[i]}')
    print(f'Player 2s hand is: {player2[i]}')