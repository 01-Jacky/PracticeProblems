"""
Find 12
1 2 3 7 5
1 3 6 13 18
1 3 6 13 woops

13... is there a 1?

value -> index
1 -> 0
2 -> 1
...

"""


# def findLongestSubarrayBySum(s, arr):
#     dp = [0] * len(arr)
#     best_so_far_map = {}
#
#     dp[0] = arr[0]
#     best_so_far_map[arr[0]] = 0
#
#     for i in range(1, len(arr)):
#         # take it or take the previous
#         cur_max = max(arr[i], arr[i] + dp[i - 1])
#         dp[i] = cur_max
#         best_so_far_map[arr[i]] = i
#
#         if cur_max == s:
#             return [1, i + 1]
#         if cur_max > s:
#             need = cur_max - s
#
#             if i == 45:
#                 print(dp)
#                 # print('cur max = {}'.format(cur_max))
#                 print('need {}'.format(need))
#                 # print(best_so_far_map)
#
#             if need in best_so_far_map:
#                 print('{} {}'.format(best_so_far_map[need]+1,i+1))
#                 return [best_so_far_map[need] + 2, i + 1]
#     return -1

def findLongestSubarrayBySum(s, arr):
    ans = []
    n = len(arr)
    curr_sum = arr[0]
    start = 0

    i = 1
    while i <= n:
        while curr_sum > s and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == s:
            # Post process 0s
            while i+1 <= n and arr[i] == 0:
                i += 1
            ans.append([start+1, i])
            # return[start+1, i]

        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    # Look at all the answer and find the longest one
    if len(ans) == 0:
        return [-1]
    else:
        # find longest answer
        answer = ans[0]
        longest_ans = ans[0][1] - ans[0][0]
        for el in ans:
            ans_length = el[1] - el[0]
            if ans_length > longest_ans:
                longest_ans = ans_length
                answer = el

        return answer



arr = [0, 1, 0, 1, 3]
# arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
# arr = [0,3,0]
# arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 0, 172, 0, 139, 0, 0, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
arr = [22, 123, 113, 49, 19, 169, 118, 115, 51, 91, 136, 160, 170, 96, 104, 41, 180, 200, 106, 192, 62, 82, 53, 154, 34, 30, 188, 43, 54, 84, 21, 15, 119, 45, 64, 30, 53, 65, 170, 71, 6, 48, 195, 88]
x = arr[21:31]
print(x)
print(sum(x))
x = arr[29:41]
print(x)
print(sum(x))
print(findLongestSubarrayBySum(743, arr))