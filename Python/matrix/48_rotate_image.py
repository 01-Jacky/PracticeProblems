import matrix_helper

"""
1) Flip and transpose
    a a a a
    b b b b
    c c c c
    d d d d
    
    flip        transpose
    d d d d     d c a b
    c c c c     d c a b
    a a a a     d c a b
    b b b b     d c a b
    
    o Y Y Y		i = 0 j = 1,2,3
    Y x x x
    Y x x x
    Y x x x
    
    o o o o		i = 1 j = 2,3
    o o Y Y
    o Y x x
    o Y x x
    
    o o o o		i = 2 j = 3
    o o o o
    o o o Y
    o o Y x
    
    o o o o		i = 3 j = 4
    o o o o
    o o o o
    o o o x

"""
class Solution(object):
    def rotate_memory_version(self, matrix):
        """
        uses memory
        clockwise rotate = flip and transpose
        """
        return zip(*matrix[::-1])

    def rotate(self, matrix):
        """
        in place
        clockwise rotate = flip and transpose
        """
        # Flip or just use matrix.reverse(), which is still O(n)
        j = len(matrix) - 1
        for i in range(len(matrix)):
            matrix[i], matrix[j] = matrix[j], matrix[i]
            j -= 1

        # Transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# ans = Solution().rotate([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ])

arr = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8],
 [ 9, 10, 11, 12],
 [ 13, 14, 15, 16]
]

Solution().rotate(arr)
matrix_helper.print_matrix(arr)
# matrix_helper.print_matrix(Solution().rotate_memory_version(arr))