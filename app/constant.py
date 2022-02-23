import os
import sys

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
ICON = os.path.join(ROOT_DIR, 'resources/blackjack-icon.png')
BACKGROUND = 'black'
FOREGROUND = 'white'
FONT = ['Helvetica', 16]
DECK = 'standard'
HEIGHT = 600
WIDTH = 800
CARD_BACK = 'back.png'
CARD_HEIGHT = 200
CARD_WIDTH = 75
CARD_SPACING = 100
BUFFER_HEIGHT = 25
BUFFER_WIDTH = 50
