import collections
def maxSlidingWindow( nums, k):
    d = collections.deque()
    out = []

    for i, n in enumerate(nums):
        print(d)
        while d and nums[d[-1]] < n:
            d.pop()
        d.append(i)

        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out.append(nums[d[0]])

    return out

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        res = []
        dq = deque()                            # store index

        for i in range(len(nums)):
            if dq and dq[0] < (i-k+1):          # out of the window e.g. k=3 i=5, (i-k+1)=3 only keep window index 3-5
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)

            if i > (k-2):                       # 0 1 2      k-2 = 4-2 = 2
                res.append(nums[dq[0]])
        return res


# arr = [1,3,-1,-3,5,3,6,7]
arr = [5,3,4,1,6,2,2,4,3,1,5]
print(Solution().maxSlidingWindow(arr, 3))