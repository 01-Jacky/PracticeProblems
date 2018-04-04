import matrix_helper

class Solution(object):
    def clear_cluster(self, grid, row, col):
        grid[row][col] = '0'
        width = len(grid[0])-1
        height = len(grid)-1

        # matrix_helper.print_matrix(grid)
        if col+1 <= width and grid[row][col+1] == '1':      # Right square
            self.clear_cluster(grid, row, col+1)
        if row+1 <= height and grid[row+1][col] == '1':     # Bottom square
            self.clear_cluster(grid, row+1, col)
        if col-1 > -1 and grid[row][col-1] == '1':          # Left square
            self.clear_cluster(grid, row, col-1)
        if row-1 > -1 and grid[row-1][col] == '1':          # Up square
            self.clear_cluster(grid, row-1, col)

    def clear_cluster(self,grid, row, col):


    def numIslands(self, grid):
        island_count = 0

        # Traverse each tile
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':     # If tile is 1, trigger a DFS
                    print('doing search')
                    matrix_helper.print_matrix(grid)
                    self.clear_cluster(grid, row, col)
                    matrix_helper.print_matrix(grid)

                    island_count += 1

        return island_count


arr = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

arr2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]

arr3 = [
    ["0", "1", "0"],
    ["1", "0", "1"],
    ["0", "1", "0"]
]

print(Solution().numIslands(arr3))