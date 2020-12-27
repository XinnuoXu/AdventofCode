#coding=utf8

def load_data(filename):
    with open(filename, 'r') as f:
        players = f.read().strip()
    [player_1, player_2] = players.split('\n\n')
    player_1 = [int(card) for card in player_1.split('\n')[1:]]
    player_2 = [int(card) for card in player_2.split('\n')[1:]]
    return player_1, player_2

def play_game(player_1, player_2):
    while (len(player_1) > 0 and len(player_2) > 0):
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        elif card_1 < card_2:
            player_2.append(card_2)
            player_2.append(card_1)
    if len(player_1) > 0:
        return player_1
    else:
        return player_2

def recursive_game(player_1, player_2):
    player_1_memory = set()
    player_2_memory = set()
    while (len(player_1) > 0 and len(player_2) > 0):
        if ''.join([str(c) for c in player_1]) in player_1_memory:
            return 'player_1', player_1
        if ''.join([str(c) for c in player_2]) in player_2_memory:
            return 'player_1', player_1
        player_1_memory.add(''.join([str(c) for c in player_1]))
        player_2_memory.add(''.join([str(c) for c in player_2]))
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        if len(player_1) >= card_1 and len(player_2) >= card_2:
            tmp_1 = player_1[:card_1]
            tmp_2 = player_2[:card_2]
            winner, _ = recursive_game(tmp_1, tmp_2)
        else:
            if card_1 > card_2:
                winner = 'player_1'
            else:
                winner = 'player_2'
        if winner == 'player_1':
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
    if len(player_1) > 0:
        return 'player_1', player_1
    else:
        return 'player_2', player_2

def count_score(cards):
    weights = np.array(range(len(cards), 0, -1))
    cards = np.array(cards)
    return (weights*cards).sum()

if __name__ == '__main__':
    import numpy as np
    player_1, player_2 = load_data('day_22.txt')
    #cards = play_game(player_1, player_2)
    #score = count_score(cards)
    #print (score)
    _, cards = recursive_game(player_1, player_2)
    score = count_score(cards)
    print (score)
