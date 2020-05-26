from blackjack.common.constant import constant
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

    player_label = Label(root, bg=constant.BACKGROUND, fg=constant.FOREGROUND, font=constant.FONT, text='Your hand:')
    player_label.grid(row=0, sticky=NW)

    player_canvas = Canvas(root, bg=constant.BACKGROUND, highlightbackground=constant.BACKGROUND,
                           height=constant.CARD_HEIGHT + constant.BUFFER_HEIGHT, width=constant.WIDTH)
    player_canvas.grid(row=1)

    cards = list()
    cards.append(get_image('s10.png'))
    cards.append(get_image('s11.png'))
    cards.append(get_image('s12.png'))
    cards.append(get_image('s13.png'))
    cards.append(get_image('s01.png'))

    x = 0

    for card in cards:
        player_canvas.create_image(x + constant.BUFFER_WIDTH, constant.BUFFER_HEIGHT, anchor=NW, image=card)
        x += constant.CARD_SPACING

    computer_label = Label(root, bg=constant.BACKGROUND, fg=constant.FOREGROUND, font=constant.FONT,
                           text="Opponent's hand:")
    computer_label.grid(row=2, sticky=NW)

    computer_canvas = Canvas(root, bg=constant.BACKGROUND, highlightbackground=constant.BACKGROUND,
                             height=constant.CARD_HEIGHT + constant.BUFFER_HEIGHT, width=constant.WIDTH)
    computer_canvas.grid(row=3)

    x = 0

    for card in cards:
        computer_canvas.create_image(x + constant.BUFFER_WIDTH, constant.BUFFER_HEIGHT, anchor=NW, image=card)
        x += constant.CARD_SPACING

    # Redraw
    root.mainloop()


def get_image(filename, deck=constant.DECK):
    file = os.path.join(constant.ROOT_DIR, f'resources/{deck}/{filename}')
    image = PhotoImage(file=file)

    return image
