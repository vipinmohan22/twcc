def draw_grid(n, m):
    tmpstr = ""
    if m >= 1:
        for j in range(0, n+1):
            for i in range(0, m+1):
                if i is not m:
                    tmpstr += "+ - "
                else:
                    tmpstr += "+" + "\n"
                if i == m:
                    if j < n:
                        for k in range(0, m + 1):
                            if k is not m:
                                tmpstr += "|   "
                            else:
                                tmpstr += "|" + "\n"
    return tmpstr



unit_square = """\
+ - +
|   |
+ - +
"""

grid_2_3 = """\
+ - + - + - +
|   |   |   |
+ - + - + - +
|   |   |   |
+ - + - + - +
"""

assert draw_grid(1, 1) == unit_square
assert draw_grid(2, 3) == grid_2_3


def draw_board(n, m):
    tmpstr = ""
    if m >= 1:
        for j in range(0, n + 1):
            if j % 2 == 0:
                toggle = True
            else:
                toggle = False
            for i in range(0, m+1):
                # import pdb; pdb.set_trace()
                if i is not m:
                    print("+ - ", end='')
                    tmpstr += "+ - "
                else:
                    print("+")
                    tmpstr += "+" + "\n"
                if i == m:
                    if j < n:
                        for k in range(0, m + 1):
                            if k is not m:
                                if toggle:
                                    print("|   ", end='')
                                    tmpstr += "|   "
                                    toggle = False
                                else:
                                    print("| B ", end='')
                                    tmpstr += "| B "
                                    toggle = True

                            else:
                                print("|")
                                tmpstr += "|" + "\n"
    return tmpstr


draw_board(n, m)

board_2_3 = """\
+ - + - + - +
|   | B |   |
+ - + - + - +
| B |   | B |
+ - + - + - +
"""

assert draw_board(1, 1) == unit_square
assert draw_board(2, 3) == board_2_3
