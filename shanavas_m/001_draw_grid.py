#!/usr/bin/env python3


def draw_grid(rows, cols):
    """
    Return string of ROWS X COLUMNS grids
    """
    # horizontal line
    hor = "+ - " * cols + "+\n"
    # vertical line
    ver = "|   " * cols + "|\n"

    return (hor + ver) * rows + hor.rstrip()


def draw_board(rows, cols):
    """
    Return string of ROWS X COLUMNS chessboard
    """
    board = ""

    # horizontal line
    hor = "+ - " * cols + "+\n"

    # vertical line for even rows
    vert_eve = "".join(["| B " if i % 2 else "|   " for i in range(cols)]) + "|\n"

    # vertical line for odd rows
    vert_odd = "".join(["|   " if i % 2 else "| B " for i in range(cols)]) + "|\n"

    for i in range(rows):
        board += hor + (vert_odd if i % 2 else vert_eve)

    return board + hor.rstrip()


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
