#!/usr/bin/env python3


def draw_grid(rows, colums):
    """
    Return string of ROWS X COLUMNS grids
    """
    pass


def draw_board(rows, colums):
    """
    Return string of ROWS X COLUMNS chessboard
    """
    pass


# tests
unit_square = """\
+ - +
|   |
+ - +"""

grid_2_3 = """\
+ - + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +"""

assert draw_grid(1, 1) == unit_square
assert draw_grid(2, 3) == grid_2_3

board_2_3 = """\
+ - + - + - +
|   | B |   |
+ - + - + - +
| B |   | B |
+ - + - + - +"""


assert draw_board(1, 1) == unit_square
assert draw_board(2, 3) == board_2_3
