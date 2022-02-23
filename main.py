#!/usr/bin/python
# coding: utf-8

__author__ = 'SLCIT Inc.'
__email__ = 'simoncharest@gmail.com'
__copyright__ = f'© {__author__}. All rights reserved.'
__project__ = 'Blackjack'
__credits__ = ['Miguel de Cervantes']
__license__ = 'GNU'
__maintainer__ = 'Simon Charest'
__status__ = 'Developement'
__version__ = '2.0.0'

from app import cli, gui


def main():
    cli.run()
    # gui.run()


if __name__ == '__main__':
    main()
