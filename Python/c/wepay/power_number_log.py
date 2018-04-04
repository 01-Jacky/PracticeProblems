"""
A PowerNumber is defined as a number greater than zero that can be expressed as X^Y, where X and Y are integers greater than one.
Create a function takes in an integer i and returns the (zero-indexed) ith power number

Write a function that returns the nth power number, where a power number is a number that can be expressed as x^y.
Note that the power number sequence is in ascending order (4, 8, 9, 16, 27, 32, ...).
"""

import math
import time

def is_power_number(n):
    # e.g. to check 10 we don't need to check all the bases from 2 to 10 because after base 4, everything is > 10.
    # Therefore the biggest base we need to check is just floor(sqrt(n))
    biggest_possible_base = int(math.sqrt(n)) + 1

    # Check each possible base
    for base in range(2, biggest_possible_base):
        # base^pow = n or log(n,base) = pow. If pow is a whole number we know base^pow = n
        power = math.log(n, base)

        if float.is_integer(power):
            return True

    return False


def nth_power_number(n):
    # power_nums = [None] * nth_power_number
    sequential_num = 1
    nth_power_number = None

    for i in range(n+1):
        while not is_power_number(sequential_num):
            sequential_num += 1

        # power_nums[i] = sequential_num
        nth_power_number = sequential_num
        # print(sequential_num)
        sequential_num += 1

    # return power_nums[-1]
    return nth_power_number

start = time.time()
print(nth_power_number(300))
end = time.time()
print(end-start)

# for i in range(10):
#     print(is_power_number(i))

# print(is_power_number(4))
# print(is_power_number(8))
# print(is_power_number(49))
# print(is_power_number(48))