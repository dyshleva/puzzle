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
        if len(set(numbers.replace(" ",""))) != len(numbers.replace(" ","")):
            return False
        i+=1
    return True

if __name__ == "__main__":
    from doctest import testmod
    print(testmod())
