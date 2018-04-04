def _valid_subsquare(grid, i,j):
    seen = set()

    for i_offset in range(3):
        for j_offset in range(3):
            r = i + i_offset
            c = j + j_offset

            if grid[r][c] == '.':
                continue
            elif grid[r][c] in seen:
                return False
            else:
                seen.add(grid[r][c])

    return True

def sudoku2(grid):
    dim = len(grid)

    # Check subsquare
    for i in range(0,dim,3):
        for j in range(0,dim,3):
            # print("check subsquare starting {} {}".format(i,j))
            if not _valid_subsquare(grid, i,j):
                return False
    print('subsquare valid')

    # Check row
    for i in range(dim):
        row_seen = set()
        for j in range(dim):
            if grid[i][j] == '.':
                continue
            elif grid[i][j] in row_seen:
                return False
            else:
                row_seen.add(grid[i][j])
    print('row valid')

    # Check column
    for i in range(dim):
        row_seen = set()
        for j in range(dim):
            if grid[j][i] == '.':
                continue
            elif grid[j][i] in row_seen:
                return False
            else:
                row_seen.add(grid[j][i])
    print('column valid')

    return True


grid =\
[[".","4",".",".",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."],
 [".",".",".","1",".",".","7",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".","3",".",".",".","6","."],
 [".",".",".",".",".","6",".","9","."],
 [".",".",".",".","1",".",".",".","."],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","8",".",".",".",".","."]]
print(sudoku2(grid))