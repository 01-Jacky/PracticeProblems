"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.

Example

For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
sumInRange(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.
"""


def sumInRange(nums, queries):
    sum_up_to_index = [0] * len(nums)
    cur_sum = 0

    # Build dp array
    for i in range(len(nums)):
        cur_sum += nums[i]
        sum_up_to_index[i] = cur_sum

    # Get query sums using dp array
    query_sums = [0] * len(queries)
    for i in range(len(queries)):
        start = queries[i][0]
        stop = queries[i][1]

        if start == 0:
            query_sums[i] = sum_up_to_index[stop]
        else:
            query_sums[i] = sum_up_to_index[stop] - sum_up_to_index[start - 1]

    return sum(query_sums) % ((10 ** 9) + 7)
