"""
9
1)
1 9
mid = (9+9-1)/2 = 17//2 = 8
9 // 2 = 4
look left
2)
1 8


1 10 = 11//2

"""

class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        left = 1
        right = x
        ans = None

        while left <= right:
            mid = (left+right) // 2

            # in other language might need to work around overflow with mid <= x/mid
            if mid*mid <= x:     # if mid^2 too small, answer os bigger
                left = mid+1
                ans = mid
            else:
                right = mid-1

        return ans


print(Solution().mySqrt(9))

