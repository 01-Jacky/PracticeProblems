"""
Given:  [−10,−10,1,3,2]
Return: 300

Given:  [1,2,3,4,5]
Return: 60

Solution:
0) Sort and find max 3 versus min 2 * max 
Time O(nlgn) Space O(n)

1) Analyze by cases:
If all pos num
    3 biggest num
If all neg num
    3 biggest num
If mix
    if only 1 neg num (that means there's 3 pos num to pick from)
        3 biggest num
    if > 1 neg num
        1 max pos num, 2 biggest neg num
So only need to save 3 biggest num and 2 biggest neg num (2 smallest num)
Time O(n) Space O(n)

2) Greedy: keep track of all those and calc best ans
Need to store:
    3 biggest pos
    3 smallest neg
    2
Time O(n) Space O(n)

3) Sort and find

"""

def maximumProduct(nums):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max1, max2, max3 = num, max1, max2
        elif num > max2:
             max2, max3 = num, max2
        elif num > max3:
            max3 = num

        if num < min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num

        product_3_max = max1 * max2 * max3
        product_2_neg_1_max = min1 * min2 * max1
    return max(product_3_max, product_2_neg_1_max)


def highest_product_of_3_v2(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for current in list_of_ints[3:]:
        # do we have a new highest product of 3? it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3



print(highest_product_of_3_v2([-10,-10,1,3,2]))
print(maximumProduct([-10,-10,1,3,2]))
# print(maximumProduct([1,2,3,-10]))


