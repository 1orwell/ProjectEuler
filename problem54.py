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
                    print(f'the index is {i} and the card is {card}')
                    play.append(card)
                    if i == 4:
                        print(f'finishing player1, hand is {play}')
                        player1[line_index+1] = play
                        play = []
                    if i == 9:
                        print(f'finishing player2, hand is {play}')
                        player2[line_index+1] = play
                        play = []
    return (player1, player2)

(player1, player2) = translate_file('p054_poker.txt')
print(f'The dictionary for player1 hand is: {player1}\n')
print(f'The dictionary for player2 hand is: {player2}\n')