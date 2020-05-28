from blackjack.common.datetime_ import datetime
import os
import sys

__author__ = 'SLCIT inc'
__email__ = 'simoncharest@gmail.com'
__copyright__ = f'Copyright © {datetime.get_years(2019)} {__author__} <{__email__}>. All rights reserved.'
__project__ = 'Blackjack'
__credits__ = ['Miguel de Cervantes']
__license__ = 'GNU'
__maintainer__ = 'Simon Charest'
__status__ = 'Developement'
__version__ = '2.0.0'

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
ICON = os.path.join(ROOT_DIR, 'resources/blackjack-icon.png')
BACKGROUND = 'black'
FOREGROUND = 'white'
FONT = ['Helvetica', 16]
DECK = 'cloisters'
#DECK = 'standard'
HEIGHT = 600
WIDTH = 800
CARD_BACK = 'back.png'
CARD_HEIGHT = 200
CARD_WIDTH = 75
CARD_SPACING = 100
BUFFER_HEIGHT = 25
BUFFER_WIDTH = 50

"""
Deck:
    Ranks:
        King
        Queen
        Jack (Knave)
    Suits:
        Club (Hound Tethers)
        Heart (Hunting Horns)
        Spade (Game Nooses)
        Diamond (Dog Collars)
    Colors:
        Club: green
        Diamond: blue
        Heart: Red
        Spade: black
Sources:
    Four-color deck (https://en.wikipedia.org/wiki/Four-color_deck)
    Ogre Battle Saga Wiki - Tarot Cards (https://ogrebattlesaga.fandom.com/wiki/Tarot_Cards)
    Rider-Waite tarot deck (https://en.wikipedia.org/wiki/Rider-Waite_tarot_deck)
    Standard 52-card deck (https://en.wikipedia.org/wiki/Standard_52-card_deck)
    Tarot Nouveau (https://en.wikipedia.org/wiki/Tarot_Nouveau)
    Tarot of Marseilles (https://en.wikipedia.org/wiki/Tarot_of_Marseilles)
    The Cloisters Playing Cards (https://www.metmuseum.org/art/collection/search/475513)
"""
