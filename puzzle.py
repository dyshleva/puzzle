def line_check(board):
    pass

def column_check(board):
    pass

def block_check(board):
    pass

def final_check(board: list) -> bool:
    """
    >>> final_check([\
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
    >>> final_check([\
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


