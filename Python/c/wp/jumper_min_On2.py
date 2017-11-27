from collections import deque

# Idea: Analyze solution in chunks
# Starting at A[0], the chunk to consider is from 0 to the furthest which is 0 + A[0].
# In that chunk, the index providing the furthest jump (i + A[i]) will be part to the solution.
# The next chunk to consider would be from the end of the chunk to the new furthest reachable index.
#
# This works and is optimal because each chunk's upper bound considered all possibilities in the previous.
# Also taking more than 1 jump between chunk would be suboptimal.
#
# Example:
#   A[0] = 5 then consider numbers in index 0-5.
#   From that range, pick the index that gets us furthest (i.e. one w/ largest i + A[i])
#   It happens to be at index 5 and A[5] = 4, so new furthest = 5 + 4 = 9.
#   Record that index 5 was our next hop.
#
#   The next "chunk" will be between previous max reachable +1 and the new max reachable
#   Rinse and repeat
#
# Time: O(n) solution because we only iterated through nums once
# Space: O(1)

class Solution(object):
    def _get_best_index(self, nums, chunk_start, chunk_end):
        """ Returns a tuple of best index and its max reach for a given chunk in the array """
        index_of_max = -1  # Index associated with the max_reach
        max_reach = -1
        for x in range(chunk_start, chunk_end + 1):  # Find the best index in the next chunk
            if x + nums[x] > max_reach:
                max_reach = x + nums[x]
                index_of_max = x
        return index_of_max, max_reach

    def jump(self, nums):
        if len(nums) == 0:
            return 'failure'

        i = 0
        max_reach = nums[i]
        solution = ['0']

        while i < len(nums)-1:
            if max_reach <= i:
                return 'failure'
            if max_reach >= len(nums):
                break                                   # Avoid analyzing unnecessarily chunks e.g. [100, 1, 1, 1]

            chunk_start = i+1
            chunk_end = min(max_reach, len(nums)-1)

            index_of_max = -1                           # Index associated with the max_reach
            for x in range(chunk_start, chunk_end+1):   # Find the best index in the next chunk
                if x+nums[x] > max_reach:
                    max_reach = x + nums[x]
                    index_of_max = x
            solution.append(str(index_of_max))
            i = chunk_end

            print(max_reach)
            print(' --- ')

        if max_reach > len(nums)-1:                 # Must hop beyond last index to succeed
            return ', '.join(solution + ['out'])
        else:
            return 'failure'




# print(Solution().jump([0]))
print(Solution().jump([5,6,0,4,2,4,1,0,0,4]))
# print(Solution().jump([1000,1,1]))
# print(Solution().jump([2,0,0,0,4]))
# print(Solution().jump([2,3,1,1,2,4,2,0,1,1]))
# Solution().jump([1,3,1,1,4])
# print(Solution().jump([1,1,1,1,1,1]))
# print(Solution().jump([2,1]))
# print(Solution().jump([1,2,3]))

