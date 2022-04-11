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

(player1, player2) = translate_file('p054_poker.txt')
#print(f'The dictionary for player1 hand is: {player1}\n')
#print(f'The dictionary for player2 hand is: {player2}\n')

for i in range(1, 1001):
    print(f'The round is {i}')
    print(f'Player 1s hand is: {player1[i]}')
    print(f'Player 2s hand is: {player2[i]}')