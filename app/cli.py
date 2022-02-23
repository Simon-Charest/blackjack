from app import game
import os


def run():
    # Initialize game
    deck = game.initialize_deck()
    player_hand = []
    opponent_hand = []

    # Draw cards
    opponent_hand += game.draw_card(deck)
    player_hand += game.draw_card(deck)
    opponent_hand += game.draw_card(deck)
    player_hand += game.draw_card(deck)
    player_total = game.get_total(player_hand)

    # Show opponent's first card
    print(f'Opponent: {game.get_hand([opponent_hand[0]])}')

    # Show player hand
    print(f'You: {game.get_hand(player_hand)}')

    # Player play
    response = input('Draw a card? ')

    while player_total <= 21 and len(player_hand) < 5 and response == 'y':
        player_hand += game.draw_card(deck)
        player_total = game.get_total(player_hand)

        # Show player hand
        print(f'You: {game.get_hand(player_hand)}')

        if player_total <= 21 and len(player_hand) < 5:
            response = input('Draw a card? ')

    # Opponent play
    opponent_total = game.get_total(opponent_hand)

    if player_total <= 21:
        while opponent_total < 17 and len(opponent_hand) < 5:
            opponent_hand += game.draw_card(deck)
            opponent_total = game.get_total(opponent_hand)

    # Show opponent hand
    print(f'Opponent: {game.get_hand(opponent_hand)}')

    # Show game results
    print(game.get_game_result(player_hand, opponent_hand))


def clear_screen():
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # Linux and macOS
    else:
        _ = os.system('clear')
