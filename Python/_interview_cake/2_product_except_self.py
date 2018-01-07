"""
Given     [1, 7, 3, 4]
Return    [84, 12, 28, 21]
Product of each number except for that index

1) Brute force
Time O(n^2) Space O(1)

2) Greedy - Look for overlaps/sub problems and store results
Store sums before index and after index
"""

def product_except_self(nums):
    products_before = [1] * len(nums)
    products_after = [1] * len(nums)

    # Store products before index and products after
    for i in range(1, len(nums)):
        products_before[i] = products_before[i-1] * nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        products_after[i] = products_after[i+1] * nums[i+1]

    # Combine the two
    for i in range(len(products_before)):
        products_before[i] *= products_after[i]

    return products_before

nums = [1, 7, 3, 4]
# nums = [3, 1, 2, 5, 6, 4]
# nums = [1, 2, 6, 5, 9]
print(product_except_self(nums))