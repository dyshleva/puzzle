def line_check(board: list) -> bool:
    '''
    Check for same digits in row
    :param (board) : input board
    :param (return) : True if no same digits else False
    >>> line_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> line_check(["**** ****", "***1 ****", "**  321**", "* 4 111**", "     9 5 ", " 67383  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    board = [row.replace('*', '').replace(' ', '') for row in board] 
    result = [set(row.replace('*', '').replace(' ', '')) for row in board]
    for index, elem in enumerate(board):
        if len(elem) != len(result[index]):
            return False
    return True

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

