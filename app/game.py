import random


def draw_card(deck):
    card_id = random.randint(0, len(deck) - 1)
    card = deck[card_id]
    deck.remove(card)

    return [card]


def get_game_result(player_hand, opponent_hand):
    player_total = get_total(player_hand)
    opponent_total = get_total(opponent_hand)

    if player_total <= 21 < opponent_total:
        game_result = 'Opponent busted: Win'

    elif player_total > 21 >= opponent_total:
        game_result = 'You busted: Lose'

    # Five-Card Charlie Rule

    elif len(player_hand) >= 5 > len(opponent_hand):
        game_result = 'You have five cards: Win'

    elif len(player_hand) < 5 <= len(opponent_hand):
        game_result = 'Opponent has five cards: Lose'

    elif len(player_hand) >= 5 <= len(opponent_hand):
        game_result = 'Both players have five cards: Tie'

    elif player_total > opponent_total:
        game_result = 'You have a better hand: Win'

    elif player_total == opponent_total:
        game_result = 'Both players have equivalent hands: Tie'

    else:
        game_result = 'Opponent has a better hand: Lose'

    return game_result


def get_hand(hand):
    total = get_total(hand)

    return f'{hand} {total}'


def get_total(cards):
    cards = sort_cards(cards)
    total = 0

    for card in cards:
        if card[0] == 'A':
            if total + get_value(card)[1] <= 21:
                total += int(get_value(card)[1])

            else:
                total += int(get_value(card)[0])

        else:
            total += int(get_value(card))

    return total


def get_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10

    elif card[0] == 'A':
        return [1, 11]

    else:
        return card[0]


def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♣', '◆', '♥', '♠']
    deck = []

    for rank in ranks:
        for suit in suits:
            deck += [(rank, suit)]

    return deck


def sort_cards(cards):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    sort_map = {rank: x for x, rank in enumerate(ranks)}

    return sorted(cards, key=lambda card: (sort_map[card[0]], card[1]))
