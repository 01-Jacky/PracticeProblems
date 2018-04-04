def add_ships(grid, S):
    # parse S into positions
    ships = S.split(',')

    for shipID, ship in enumerate(ships,1):
        tmp = ship.split(' ')
        start_pos = tmp[0]
        end_pos = tmp[1]

        if len(start_pos) == 2:
            start_row_ch = start_pos[0]
            start_col_ch = start_pos[1]
            end_row_ch = end_pos[0]
            end_col_ch = end_pos[1]
        else:
            start_row_ch = start_pos[0:2]
            start_col_ch = start_pos[2]
            end_row_ch = end_pos[0:2]
            end_col_ch = end_pos[2]

        # Convert start and stop to indexes
        start_row_index = int(start_row_ch) - 1
        start_col_index = ord(start_col_ch) - ord('A')
        end_row_index = int(end_row_ch) - 1
        end_col_index = ord(end_col_ch) - ord('A')

        for i in range(start_row_index,end_row_index+1):
            for j in range(start_col_index, end_col_index+1):
                grid[i][j].append(shipID)


def add_targets(grid, T):
    if T == '':
        return

    targets = T.split(' ')

    for target in targets:
        if len(target) == 2:
            row_ch = target[0]
            col_ch = target[1]
        else:
            row_ch = target[0:2]
            col_ch = target[2]

        # Convert start and stop to indexes
        row = int(row_ch) - 1
        col = ord(col_ch) - ord('A')

        grid[row][col].append('hit')


def solution(N, S, T):
    grid = []
    for i in range(N):
        sets = [[] for _ in range(N)]
        grid.append(sets)

    # Fill out grid with ship and targets
    add_ships(grid, S)
    add_targets(grid,T)

    # Tally each ships hp and hits against them
    ship_hp = {}
    ship_dmg = {}
    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) != 0:
                ship_num = grid[i][j][0]

                if ship_num not in ship_hp:
                    ship_hp[ship_num] = 1
                else:
                    ship_hp[ship_num] += 1

            if len(grid[i][j]) == 2:
                if ship_num not in ship_dmg:
                    ship_dmg[ship_num] = 1
                else:
                    ship_dmg[ship_num] += 1

    # Infer if ship is sunk or damaged from hp and damage
    damaged = 0
    sunk = 0
    for ship_num in ship_hp:
        if ship_num in ship_dmg:
            if ship_hp[ship_num] == ship_dmg[ship_num]:
                sunk += 1
            else:
                damaged += 1

    return '{},{}'.format(sunk,damaged)




N = 4
S = "1B 2C,2D 4D"
T = "2B 2D 3D 4D 4A"

# N = 3
# S = "1A 1B,2C 2C"
# T = "1B"

N = 12
S = "1A 2A,12A 12A"
T = ""
print(solution(N,S,T))