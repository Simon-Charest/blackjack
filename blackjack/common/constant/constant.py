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

"""
Deck:
    Values:
        King
        Queen
        Jack (Knave)
    Kinds:
        Club (Hound Tethers)
        Heart (Hunting Horns)
        Spade (Game Nooses)
        Diamond (Dog Collars)
Source: The Cloisters Playing Cards (https://www.metmuseum.org/art/collection/search/475513)
"""
