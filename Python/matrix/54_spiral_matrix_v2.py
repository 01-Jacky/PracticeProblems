class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        if not matrix:      # Empty input
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
#
# ans = Solution().spiralOrder([
#  [7],[9],[6],
# ])

print(ans)
