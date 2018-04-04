"""
1) Bucket sort
Generate freq map
2 -> 10     2 appeared 10 times, etc...
5 -> 2
...

Buckets from 0 to n elements (most frequent is if all element are the same). Say there's 20 elements
[[],[],... []]    20 buckets representing freq. Dump numbers with the same freq into respective buckets
e.g. 2 has 10 frequency, so add to into the 10 bucket
To get top k read backwards k times :)

2) Heap sort
Build heap in O(n)

Pull out k elements in O(k) time
"""


class Solution:
    def topKFrequent(self, nums, k):
        import heapq

        # Get freq counts
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] = freq[num] + 1

        # Store a tuple (freq, integer) to build heap off of. Switch freq's sign to do max heap
        freq_list = [(-freq[key], key) for key in freq.keys()]
        heapq.heapify(freq_list)

        # Pull top k frequent elements
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freq_list))

        return ans

print(Solution().topKFrequent([1,2,3,4,5,6,7,8,9,10,1,1,1,3,3,3,3,3,9,9],3))