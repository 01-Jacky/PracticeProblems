import random

def max_of_min_sliding_window(nums, k):
    import collections
    if not nums:
        return []

    buffer = collections.deque()        # holds index of the min elements. Head holds min at the current window
    mins = []
    max_so_far = float('-inf')

    for i in range(len(nums)):
        # discard head of buffer if it's outside the window
        if buffer and buffer[0] < (i-k+1):
            buffer.popleft()


        # push in current element and discard any element that is a worse candidate
        # e.g.  buffer [3 5 10], put in 4, we throw out 5 and 10 and end up with [3, 4] because
        #       we know we don't need to keep 10 and 5 as 4 is smaller than both
        while buffer and nums[i] < nums[buffer[-1]]:
            buffer.pop()
        buffer.append(i)

        # min of the current window is at the head. Copy it to the answer.
        min_current_window = nums[buffer[0]]
        if i > (k - 2):
            mins.append(min_current_window)
            max_so_far = max(max_so_far, min_current_window)

    print(mins)
    return max_so_far


arr = [1, 3, -1, -3, 5, 3, 6, 7]
# arr = [5,3,4,1,6,2,2,4,3,1,5]
arr = [random.randint(-10,10) for _ in range(9)]
print(arr)
print(max_of_min_sliding_window(arr, 2))