def line_check(board):
    pass

def column_check(board: list) -> bool:
    """
    cehck column
    >>> column([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   9  **",\
    "  8  2***",\
    "  2  ****"\
    ])
    True
    >>> column([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"\
    ])
    False
    """
    lst = []
    for i in range(9):
        for j in board:
            if (j[i]).isdigit():
                if j[i] not in lst:
                    lst += j[i]
                else:
                    return False
        lst = []
    return True

def block_check(board):
    pass

def final_check(board):
    pass

