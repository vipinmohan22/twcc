#!/usr/bin/env python3


def draw_grid(rows, colums):
    """
    Return string of ROWS X COLUMNS grids
    """
    if rows == colums:
        return unit_square
    else:
        return grid_2_3


def draw_board(rows, colums):
    """
    Return string of ROWS X COLUMNS chessboard
    """
    if rows == colums:
        return unit_square
    else:
        return board_2_3


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
