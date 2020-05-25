import os
import random


def execute():
    # Initialize game
    deck = initialize_deck()
    player_hand = []
    opponent_hand = []

    # Draw cards
    opponent_hand += draw_card(deck)
    player_hand += draw_card(deck)
    opponent_hand += draw_card(deck)
    player_hand += draw_card(deck)
    player_total = get_total(player_hand)

    # Show player hand
    os.system('clear')
    print('You:')
    show_hand(player_hand)

    # Player play
    response = input('Draw a card? ')

    while player_total <= 21 and len(player_hand) < 5 and response == 'y':
        player_hand += draw_card(deck)
        player_total = get_total(player_hand)

        # Show player hand
        os.system('clear')
        print('You:')
        show_hand(player_hand)

        if player_total <= 21 and len(player_hand) < 5:
            response = input('Draw a card? ')

    # Opponent play
    opponent_total = get_total(opponent_hand)

    if player_total <= 21:
        while opponent_total < 17 and len(opponent_hand) < 5:
            opponent_hand += draw_card(deck)
            opponent_total = get_total(opponent_hand)

    # Show opponent hand
    print('Opponent:')
    show_hand(opponent_hand)

    # Show game results
    show_game_results(player_hand, opponent_hand)


def initialize_deck():
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    kinds = ['♣', '◆', '♥', '♠']
    deck = []

    for value in card_values:
        for kind in kinds:
            deck += [(value, kind)]

    return deck


def draw_card(deck):
    card_id = random.randint(0, len(deck) - 1)
    card = deck[card_id]
    deck.remove(card)

    return [card]


def get_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10

    elif card[0] == 'A':
        return [1, 11]

    else:
        return card[0]


def sort_cards(cards):
    # Source: https://stackoverflow.com/questions/37179737/sorting-list-of-cards
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    sort_map = {c: i for i, c in enumerate(card_values)}

    return sorted(cards, key=lambda card: (sort_map[card[0]], card[1]))


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


def show_hand(hand):
    total = get_total(hand)

    print('%s %d' % (hand, total))


def show_game_results(player_hand, opponent_hand):
    player_total = get_total(player_hand)
    opponent_total = get_total(opponent_hand)

    if player_total <= 21 < opponent_total:
        print('Opponent busted: Win')

    elif player_total > 21 >= opponent_total:
        print('You busted: Lose')

    elif player_total > opponent_total:
        print('You have a better hand: Win')

    elif len(player_hand) >= 5 > len(opponent_hand):
        print('You have five cards: Win')

    elif len(player_hand) < 5 <= len(opponent_hand):
        print('Opponent has five cards: Lose')

    elif len(player_hand) >= 5 <= len(opponent_hand):
        print('Both players have five cards: Tie')

    elif player_total == opponent_total:
        print('Both players have equivalent hands: Tie')

    else:
        print('Opponent has a better hand: Lose')
