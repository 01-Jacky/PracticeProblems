class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        if not matrix:      # Empty input
            return ans

        row_start = 0
        row_end = len(matrix)-1
        col_start = 0
        col_end = len(matrix[0])-1

        while(row_start <= row_end and col_start <= col_end):
            for i in range(col_start, col_end+1):       # Right
                ans.append(matrix[row_start][i])
            row_start += 1

            if row_start > row_end:                     # Might not need to go down if 1xN matrix
                return ans

            for i in range(row_start, row_end+1):       # Down
                ans.append(matrix[i][col_end])
            col_end -= 1

            for i in range(col_end, col_start-1,-1):    # Left
                ans.append(matrix[row_end][i])
            row_end -= 1

            if col_start > col_end:                     # Might not need to go left if Mx1 matrix
                return ans

            for i in range(row_end, row_start-1, -1):   # Up
                ans.append(matrix[i][col_start])
            col_start += 1

        return ans


ans = Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
#

# ans = Solution().spiralOrder([
#  [2,3],
# ])

# ans = Solution().spiralOrder([
#  [7],[9],[6],
# ])

# ans = Solution().spiralOrder([
#     [1, 2], [8, 3], [7, 4], [6, 5],
# ])

print(ans)