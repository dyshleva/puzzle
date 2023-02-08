def line_check(board):
    '''
    Check for same digits in row
    :param (board) : input board
    :param (return) : True if no same digits else False
    >>> line_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> line_check(["**** ****", "***1 ****", "**  321**", "* 4 111**", "     9 5 ", " 67383  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> line_check(["**** ****", "***1 ****", "**  321**", "* 40111**", "     905 ", " 67383  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    board = [row.replace('*', '').replace(' ', '') for row in board] 
    result = [set(row.replace('*', '').replace(' ', '')) for row in board]
    for index, elem in enumerate(board):
        if len(elem) != len(result[index]) or '0' in elem:
            return False
    return True

def column_check(board: list) -> bool:
    """
    cehck column
    >>> column_check([\
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
    >>> column_check([\
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

def block_check(board:list) -> bool:
    """
    Check for same digits in color block
    Args:
        board (list): playboard
    Returns:
        bool: True if no same digits in every color block, else False
    >>> block_check([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    >>> block_check([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  22 ****"])
    False
    """
 start = [0, 8]
    for column in range(5):
        lst = [board[start[1]-column][start[0] +
                                      column+1:start[0]+5+column].replace(" ", "")]
        lst = list("".join(lst))

        sset = set(board[start[1]-column][start[0] +
                  column:start[0]+5+column].replace(" ", ""))

        new = set([board[start[1]-4-column:start[1]-column+1][i][start[0]+column].replace(" ", "")
                  for i in range(5)])
        lst += [n for n in new if n.isdigit()]
        set2 = set([n for n in new if n.isdigit()])
       
        if len(lst) != len(sset.union(set2)):
            return False
    return True


def validate_board(board: list) -> bool:
    """
    check all
    Args:
        board (list): playboard
    Returns:
        bool: True if no same digits in every color block, else False
    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   7  **",\
 "  8  2***",\
 "  2  ****"])
    True
    """
    if line_check(board) and column_check(board) and block_check(board):
        return True
    return False



