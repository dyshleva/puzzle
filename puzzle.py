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
    i = 1
    while i <= 5:
        numbers = ""
        numbers += board[-i][i-1:i+4]
        j = i
        while j <= i+4:
            numbers += board[-j][i-1]
            j += 1
        if len(set(numbers.replace(" ",""))) != len(numbers.replace(" ","")) or "0" in numbers:
            return False
        i+=1
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



