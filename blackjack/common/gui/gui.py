from blackjack.common.constant import constant
from blackjack.common.game import game
from tkinter import *
import os


def execute():
    # Display application
    root = Tk()
    root.configure(background=constant.BACKGROUND)
    root.geometry(f'{constant.WIDTH}x{constant.HEIGHT}')
    root.resizable(0, 0)  # Prevent resizing and disable maximize button
    root.title(constant.__project__)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=constant.ICON))

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
    opponent_total = game.get_total(opponent_hand)

    # Create list of images
    player_cards = get_image_list(player_hand)

    # Player
    player_label = Label(root, bg=constant.BACKGROUND, fg=constant.FOREGROUND, font=constant.FONT,
                         text=f'Your hand: {player_total}')
    player_label.grid(column=0, row=0, sticky=NW)

    # Player hand
    player_canvas = Canvas(root, bg=constant.BACKGROUND, highlightbackground=constant.BACKGROUND,
                           height=constant.CARD_HEIGHT + constant.BUFFER_HEIGHT, width=constant.WIDTH)
    player_canvas.grid(column=1, row=0)

    # Draw player cards
    paint(player_cards, player_canvas)

    opponent_label = Label(root, bg=constant.BACKGROUND, fg=constant.FOREGROUND, font=constant.FONT,
                           text=f"Opponent's hand: {opponent_total}")
    opponent_label.grid(column=0, row=1, sticky=NW)

    opponent_canvas = Canvas(root, bg=constant.BACKGROUND, highlightbackground=constant.BACKGROUND,
                             height=constant.CARD_HEIGHT + constant.BUFFER_HEIGHT, width=constant.WIDTH)
    opponent_canvas.grid(column=1, row=1)

    # Create list of images
    opponent_cards = get_image_list(opponent_hand)

    # Draw computer cards
    paint(opponent_cards, opponent_canvas)

    # Display button
    draw_button = Button(root, font=constant.FONT, height=2, width=15, text='Draw', command=lambda: draw())
    draw_button.grid(column=0, row=2)

    # Display button
    stand_button = Button(root, font=constant.FONT, height=2, width=15, text='Stand', command=lambda: stand())
    stand_button.grid(column=1, row=2)

    # Redraw
    root.mainloop()


def draw():
    print('Draw')


def stand():
    print('Stand')


def get_filename(card, extension='.png'):
    suit_name = get_suit_name(card[1])
    rank_name = get_rank_name(card[0])
    filename = f'{suit_name}{rank_name}{extension}'

    return filename


def get_image(card, deck=constant.DECK):
    filename = get_filename(card)
    file = os.path.join(constant.ROOT_DIR, f'resources/{deck}/{filename}')
    image = PhotoImage(file=file)

    return image


def get_image_list(cards):
    list_ = list()

    for card in cards:
        list_.append(get_image(card))

    return list_


def get_rank_name(rank):
    if rank == 'J':
        rank_name = '11'

    elif rank == 'Q':
        rank_name = '12'

    elif rank == 'K':
        rank_name = '13'

    elif rank == 'A':
        rank_name = '01'

    else:
        rank_name = rank.zfill(2)

    return rank_name


def get_suit_name(suit):
    if suit == '♣':
        suit_name = 'c'

    elif suit == '◆':
        suit_name = 'd'

    elif suit == '♥':
        suit_name = 'h'

    else:
        suit_name = 's'

    return suit_name


def paint(cards, canvas):
    x = 0

    for card in cards:
        canvas.create_image(x + constant.BUFFER_WIDTH, constant.BUFFER_HEIGHT, anchor=NW, image=card)
        x += constant.CARD_SPACING
