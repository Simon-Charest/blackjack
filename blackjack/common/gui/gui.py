from blackjack.common.constant import constant
from tkinter import *


def execute():
    # Display application
    root = Tk()
    root.geometry('800x600')
    root.resizable(0, 0)  # Prevent resizing and disable maximize button
    root.title(constant.__project__)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=constant.ICON))

    you_label = Label(root, text='You:')
    you_label.grid(row=0, column=0, sticky=NW)

    your_hand_label = Label(root, text='Your hand:')
    your_hand_label.grid(row=1, column=0, sticky=NW)

    opponent_label = Label(root, text='Opponent:')
    opponent_label.grid(row=2, column=0, sticky=NW)

    opponent_hand_label = Label(root, text="Opponent's hand:")
    opponent_hand_label.grid(row=3, column=0, sticky=NW)

    # Redraw
    root.mainloop()
