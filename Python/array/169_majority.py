"""
1) Sort and find
Time O(nlgn) Space O(n)

2) Hashtable
Time O(n) Space O(n)

3) Majority voting algorithm (ONLY WORKS WHEN MAJORITY IS > N/2
Time O(n) Space O(1)
"""

class Solution:
    def majorityElement(self, nums):
        """3) """
        candidate = nums[0]
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate

    def majorityElement_hash(self, nums):
        """3) """
        freq = {}

        # Count freq
        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1

        # Find majority
        majority_element = None
        max_freq = 0
        for k, v in freq.items():
            if v > max_freq:
                max_freq = v
                majority_element = k

        return majority_element

print(Solution().majorityElement([2, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8]))
print(Solution().majorityElement_hash([2, 2, 3, 3, 3, 1, 2, 3, 4, 5, 6, 7, 8]))