# A very hungry rabbit is placed in the center of of a garden, represented by a rectangular N x M 2D matrix.
# The values of the matrix will represent numbers of carrots available to the rabbit in each square of the garden.

# If the garden does not have an exact center, the rabbit should start in the square closest to the center with the
# highest carrot count.

# On a given turn, the rabbit will eat the carrots available on the square that it is on, and then move up, down, left,
# or right, choosing the the square that has the most carrots. If there are no carrots left on any of the adjacent
# squares, the rabbit will go to sleep.

# You may assume that the rabbit will never have to choose between two squares with the same number of carrots.
# Write a function which takes a garden matrix and returns the number of carrots the rabbit eats.

# You may assume the matrix is rectangular with at least 1 row and 1 column, and
# that it is populated with non-negative integers. For example,

# [[5, 7, 8, 6, 3],
# [0, 0, 7, 0, 4],
# [4, 6, 3, 4, 9],
# [3, 1, 0, 5, 8]]

# 27


def _get_start_position(m):
    """ Returns a tuple representing the x,y center of matrix or square with the most carrot closest to center """
    rows = len(m)
    cols = len(m[0])

    if rows % 2 == 1:
        x_possible = [(rows // 2)]                       # 5//2 = 2 which is already the right index, no need for -1
    else:
        x_possible = [(rows // 2) - 1, (rows // 2)]      # 4//2 = 2, so the index we want are 1,2

    if cols % 2 == 1:
        y_possible = [(cols // 2)]
    else:
        y_possible = [(cols // 2) - 1, (cols // 2)]

    most_carrot = 0
    for i in x_possible:
        for j in y_possible:
            if m[i][j] > most_carrot:
                most_carrot = m[i][j]
                x_start = i
                y_start = j

    return x_start, y_start


def _get_next_position(m, x, y):
    """ Returns a tuple of (x,y) of adjacent square (up, down, left, right) with most carrots. Or None if n """
    # See which x,y are inbound
    valid_xy = []                   # Tuples of (x,y) coordinates
    if x-1 >= 0:                    # Left
        valid_xy.append((x-1, y))
    if x+1 < len(m):                # Right
        valid_xy.append((x+1, y))
    if y-1 >= 0:                    # Up
        valid_xy.append((x, y-1))
    if y+1 < len(m[0]):             # Down
        valid_xy.append((x, y+1))

    # Go through each valid x,y and return the x,y of the one with the most carrot
    most_carrot = 0
    x_next = y_next = None
    for xy in valid_xy:
        i, j = xy                   # unpack the tuple (x,y)
        if m[i][j] > most_carrot:
            most_carrot = m[i][j]
            x_next = i
            y_next = j

    if most_carrot == 0:            # We ran out of carrots to eat
        return None, None
    else:
        return x_next, y_next


def get_carrots_eaten(m):
    """ Return the # of carrots eaten given matrix m """
    if len(m) < 1 or len(m[0]) < 1:
        return 0

    sum_eaten = 0
    x, y = _get_start_position(m)       # Could also use a dictionary or wrapper class instead of tuple

    while True:                         # Stop when _get_next_position can't find more carrots to eat
        if x is None:
            break
        print('[{}][{}] = {}'.format(x,y,m[x][y]))
        sum_eaten += m[x][y]
        m[x][y] = 0                     # Remove the eaten carrot to get the next position correctly

        x, y = _get_next_position(m, x, y)

    return sum_eaten


# m = [[1,2,3],
#      [4,5,8],
#      [7,8,9]]
# x_start, y_start = _get_start_position(m)
# print('eaten = {}'.format(get_carrots_eaten(m)))
# print()
#
# m = [[5, 7, 8, 1, 6, 3],
#      [0, 0, 7, 2, 0, 4],
#      [4, 6, 3, 3, 4, 9],
#      [3, 1, 0, 4, 5, 8],]
# x_start, y_start = _get_start_position(m)
# print('eaten = {}'.format(get_carrots_eaten(m)))

# m = [[5, 7, 8, 6, 3],
#      [0, 0, 7, 0, 4],
#      [1, 2, 3, 4, 5],
#      [4, 6, 9, 4, 9],
#      [3, 1, 0, 5, 8],
#      ]
# x_start, y_start = _get_start_position(m)
# print('eaten = {}'.format(get_carrots_eaten(m)))

m = [[5, 7, 8, 11, 16, 3],
     [0, 0, 9, 12, 0, 4],
     [4, 6, 14, 13, 4, 9],
     [3, 1, 0, 4, 5, 8],]
print('eaten = {}'.format(get_carrots_eaten(m)))