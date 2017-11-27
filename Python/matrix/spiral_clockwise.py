import matrix_helper

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        # matrix[:] = zip(*matrix[::-1])
        while matrix:
            matrix_helper.print_matrix(matrix)
            res.extend(matrix[0])
            matrix[:] = matrix[1:]
            matrix[:] = list(zip(*matrix))[::-1]
            print()
        return res


# ans = Solution().spiralOrder([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ])
# print(ans)

# ans = Solution().spiralOrder([
#  [2,3],
# ])


# ans = Solution().spiralOrder([
#  [7],[9],[6],
# ])
# print(ans)

ans = Solution().spiralOrder([
    [1, 2], [8, 3], [7, 4], [6, 5],
])
print(ans)
