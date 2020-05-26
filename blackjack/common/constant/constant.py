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
    Standard 52-card deck (https://en.wikipedia.org/wiki/Standard_52-card_deck)
    The Cloisters Playing Cards (https://www.metmuseum.org/art/collection/search/475513)
"""

DECKS = {
    'cloisters': {
        '♣A': {
            'value': [1, 11],
            'filename': 'c01.png'
        },
        '♣2': {
            'value': 2,
            'filename': 'c02.png'
        },
        '♣3': {
            'value': 3,
            'filename': 'c03.png'
        },
        '♣4': {
            'value': 4,
            'filename': 'c04.png'
        },
        '♣5': {
            'value': 5,
            'filename': 'c05.png'
        },
        '♣6': {
            'value': 6,
            'filename': 'c06.png'
        },
        '♣7': {
            'value': 7,
            'filename': 'c07.png'
        },
        '♣8': {
            'value': 8,
            'filename': 'c08.png'
        },
        '♣9': {
            'value': 9,
            'filename': 'c09.png'
        },
        '♣10': {
            'value': 10,
            'filename': 'c10.png'
        },
        '♣J': {
            'value': 10,
            'filename': 'c11.png'
        },
        '♣Q': {
            'value': 10,
            'filename': 'c12.png'
        },
        '♣K': {
            'value': 10,
            'filename': 'c13.png'
        },
        '◆A': {
            'value': [1, 11],
            'filename': 'd01.png'
        },
        '◆2': {
            'value': 2,
            'filename': 'd02.png'
        },
        '◆3': {
            'value': 3,
            'filename': 'd03.png'
        },
        '◆4': {
            'value': 4,
            'filename': 'd04.png'
        },
        '◆5': {
            'value': 5,
            'filename': 'd05.png'
        },
        '◆6': {
            'value': 6,
            'filename': 'd06.png'
        },
        '◆7': {
            'value': 7,
            'filename': 'd07.png'
        },
        '◆8': {
            'value': 8,
            'filename': 'd08.png'
        },
        '◆9': {
            'value': 9,
            'filename': 'd09.png'
        },
        '◆10': {
            'value': 10,
            'filename': 'd10.png'
        },
        '◆J': {
            'value': 10,
            'filename': 'd11.png'
        },
        '◆Q': {
            'value': 10,
            'filename': 'd12.png'
        },
        '◆K': {
            'value': 10,
            'filename': 'd13.png'
        },
        '♥A': {
            'value': [1, 11],
            'filename': 'h01.png'
        },
        '♥2': {
            'value': 2,
            'filename': 'd02.png'
        },
        '♥3': {
            'value': 3,
            'filename': 'd03.png'
        },
        '♥4': {
            'value': 4,
            'filename': 'd04.png'
        },
        '♥5': {
            'value': 5,
            'filename': 'd05.png'
        },
        '♥6': {
            'value': 6,
            'filename': 'd06.png'
        },
        '♥7': {
            'value': 7,
            'filename': 'd07.png'
        },
        '♥8': {
            'value': 8,
            'filename': 'd08.png'
        },
        '♥9': {
            'value': 9,
            'filename': 'd09.png'
        },
        '♥10': {
            'value': 10,
            'filename': 'd10.png'
        },
        '♥J': {
            'value': 10,
            'filename': 'd11.png'
        },
        '♥Q': {
            'value': 10,
            'filename': 'd12.png'
        },
        '♥K': {
            'value': 10,
            'filename': 'd13.png'
        },
        '♠A': {
            'value': [1, 11],
            'filename': 's01.png'
        },
        '♠2': {
            'value': 2,
            'filename': 'd02.png'
        },
        '♠3': {
            'value': 3,
            'filename': 'd03.png'
        },
        '♠4': {
            'value': 4,
            'filename': 'd04.png'
        },
        '♠5': {
            'value': 5,
            'filename': 'd05.png'
        },
        '♠6': {
            'value': 6,
            'filename': 'd06.png'
        },
        '♠7': {
            'value': 7,
            'filename': 'd07.png'
        },
        '♠8': {
            'value': 8,
            'filename': 'd08.png'
        },
        '♠9': {
            'value': 9,
            'filename': 'd09.png'
        },
        '♠10': {
            'value': 10,
            'filename': 'd10.png'
        },
        '♠J': {
            'value': 10,
            'filename': 'd11.png'
        },
        '♠Q': {
            'value': 10,
            'filename': 'd12.png'
        },
        '♠K': {
            'value': 10,
            'filename': 'd13.png'
        }
    },
    'standard': {
        '♣A': {
            'value': [1, 11],
            'filename': 'c01.svg'
        },
        '♣2': {
            'value': 2,
            'filename': 'c02.svg'
        },
        '♣3': {
            'value': 3,
            'filename': 'c03.svg'
        },
        '♣4': {
            'value': 4,
            'filename': 'c04.svg'
        },
        '♣5': {
            'value': 5,
            'filename': 'c05.svg'
        },
        '♣6': {
            'value': 6,
            'filename': 'c06.svg'
        },
        '♣7': {
            'value': 7,
            'filename': 'c07.svg'
        },
        '♣8': {
            'value': 8,
            'filename': 'c08.svg'
        },
        '♣9': {
            'value': 9,
            'filename': 'c09.svg'
        },
        '♣10': {
            'value': 10,
            'filename': 'c10.svg'
        },
        '♣J': {
            'value': 10,
            'filename': 'c11.svg'
        },
        '♣Q': {
            'value': 10,
            'filename': 'c12.svg'
        },
        '♣K': {
            'value': 10,
            'filename': 'c13.svg'
        },
        '◆A': {
            'value': [1, 11],
            'filename': 'd01.svg'
        },
        '◆2': {
            'value': 2,
            'filename': 'd02.svg'
        },
        '◆3': {
            'value': 3,
            'filename': 'd03.svg'
        },
        '◆4': {
            'value': 4,
            'filename': 'd04.svg'
        },
        '◆5': {
            'value': 5,
            'filename': 'd05.svg'
        },
        '◆6': {
            'value': 6,
            'filename': 'd06.svg'
        },
        '◆7': {
            'value': 7,
            'filename': 'd07.svg'
        },
        '◆8': {
            'value': 8,
            'filename': 'd08.svg'
        },
        '◆9': {
            'value': 9,
            'filename': 'd09.svg'
        },
        '◆10': {
            'value': 10,
            'filename': 'd10.svg'
        },
        '◆J': {
            'value': 10,
            'filename': 'd11.svg'
        },
        '◆Q': {
            'value': 10,
            'filename': 'd12.svg'
        },
        '◆K': {
            'value': 10,
            'filename': 'd13.svg'
        },
        '♥A': {
            'value': [1, 11],
            'filename': 'h01.svg'
        },
        '♥2': {
            'value': 2,
            'filename': 'd02.svg'
        },
        '♥3': {
            'value': 3,
            'filename': 'd03.svg'
        },
        '♥4': {
            'value': 4,
            'filename': 'd04.svg'
        },
        '♥5': {
            'value': 5,
            'filename': 'd05.svg'
        },
        '♥6': {
            'value': 6,
            'filename': 'd06.svg'
        },
        '♥7': {
            'value': 7,
            'filename': 'd07.svg'
        },
        '♥8': {
            'value': 8,
            'filename': 'd08.svg'
        },
        '♥9': {
            'value': 9,
            'filename': 'd09.svg'
        },
        '♥10': {
            'value': 10,
            'filename': 'd10.svg'
        },
        '♥J': {
            'value': 10,
            'filename': 'd11.svg'
        },
        '♥Q': {
            'value': 10,
            'filename': 'd12.svg'
        },
        '♥K': {
            'value': 10,
            'filename': 'd13.svg'
        },
        '♠A': {
            'value': [1, 11],
            'filename': 's01.svg'
        },
        '♠2': {
            'value': 2,
            'filename': 'd02.svg'
        },
        '♠3': {
            'value': 3,
            'filename': 'd03.svg'
        },
        '♠4': {
            'value': 4,
            'filename': 'd04.svg'
        },
        '♠5': {
            'value': 5,
            'filename': 'd05.svg'
        },
        '♠6': {
            'value': 6,
            'filename': 'd06.svg'
        },
        '♠7': {
            'value': 7,
            'filename': 'd07.svg'
        },
        '♠8': {
            'value': 8,
            'filename': 'd08.svg'
        },
        '♠9': {
            'value': 9,
            'filename': 'd09.svg'
        },
        '♠10': {
            'value': 10,
            'filename': 'd10.svg'
        },
        '♠J': {
            'value': 10,
            'filename': 'd11.svg'
        },
        '♠Q': {
            'value': 10,
            'filename': 'd12.svg'
        },
        '♠K': {
            'value': 10,
            'filename': 'd13.svg'
        }
    }
}
