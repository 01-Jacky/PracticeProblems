def _get_start_position(m):
    """ Returns a tuple (row,col) of center of matrix or square closest to the center w/ most carrot"""
    rows = len(m)
    cols = len(m[0])

    if rows % 2 == 1 and cols % 2 == 1:
        row_possible = [rows // 2]  # e.g. 5//2 = 2, already the index so don't need -1
    else:
        row_possible = [(rows // 2) - 1, (rows // 2)]  # e.g. 4//2 = 2, so we want 1,2

    if cols % 2 == 1:
        col_possible = [(cols // 2)]
    else:
        col_possible = [(cols // 2) - 1, (cols // 2)]

    # Check and return [row][col] with most carrot
    most_carrot = 0
    for r in row_possible:
        for c in col_possible:
            if m[r][c] > most_carrot:
                most_carrot = m[r][c]
                r_start = r
                c_start = c

    return r_start, c_start


def _get_next_position(m, row, col):
    valid_row_col = []  # Tuples of (row,col) that's valid next move
    if row - 1 >= 0:  # Check left
        valid_row_col.append((row - 1, col))
    if row + 1 < len(m):  # Right
        valid_row_col.append((row + 1, col))
    if col - 1 >= 0:  # up
        valid_row_col((row, col - 1))
    if col + 1 < len(m[0]):  # Down
        valid_row_col((row, col + 1))

    # Check and return [row][col] with most carrot
    # This is slightly different than one in _get_start_position; if there's  time refactor them to 1 helper
    most_carrot = 0
    row_next = col_next = None
    for row_col in valid_row_col
        r, c = row_col
        if m[r][c] > most_carrot:
            most_carrot = m[r][c]
            r_next = r
            c_next = c

    if most_carrot == 0:  # We ran out of carrots to eat
        return None, None
    else:
        return r_next, c_next


def get_carrots_eaten(m):
    """
    Return the # of carrots eaten given matrix m
    """
    if len(m) < 1 or len(m[0]) < 1:
        return 0

    sum_eaten = 0
    r, c = _get_start_position(m)  # Could also return a dictionary or class instead of tuple

    while True:  # Stop when _get_next_position can't find anymore carrots
        if r is None:
            break
        sum_eaten += m[r][c]
        m[r][c] = 0

        r, c = _get_next_position(m, r, c)

        return sum_eaten