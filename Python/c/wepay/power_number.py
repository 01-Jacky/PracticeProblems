"""
A PowerNumber is defined as a number greater than zero that can be expressed as X^Y, where X and Y are integers greater than one.
Create a function takes in an integer i and returns the (zero-indexed) ith power number

Write a function that returns the nth power number, where a power number is a number that can be expressed as x^y.
Note that the power number sequence is in ascending order (4, 8, 9, 16, 27, 32, ...).
"""

import math
import time

def is_power_number(n):
    # e.g. to check 10, 4^2 > 10 already so we know 4 can't be a base. Therefore the biggest base we need to check is
    # just floor(sqrt(n))
    biggest_possible_base = int(math.sqrt(n)) + 1

    for base in range(2, biggest_possible_base):
        power = 1
        check_ans = base

        while check_ans <= n:
            if check_ans == n:
                # print('{}^{}'.format(base,power))
                return True

            check_ans *= base
            power += 1

    return False


def nth_power_number(n):
    nth_power_number = n+1
    power_nums = [None] * nth_power_number
    sequential_num = 1

    for i in range(len(power_nums)):
        while not is_power_number(sequential_num):
            sequential_num += 1

        power_nums[i] = sequential_num
        sequential_num += 1

    # print(power_nums)

start = time.time()
nth_power_number(300)
end = time.time()
print(end-start)

# for i in range(10):
#     print(is_power_number(i))

# print(is_power_number(4))
# print(is_power_number(8))
# print(is_power_number(49))
# print(is_power_number(48))