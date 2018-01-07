class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        1) Use Counter object
        2) Use hashmap to account for 1st array. Then 2nd array has intersect only if it is in the 1st.
        """
        map = {}
        for num in nums1:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        intersect = []
        for num in nums2:
            if num in map and map[num] > 0:
                intersect.append(num)
                map[num] -= 1

        return intersect

print(Solution().intersect([1,2,2,3],[2,2]))