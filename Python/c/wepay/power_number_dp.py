"""
A PowerNumber is defined as a number greater than zero that can be expressed as X^Y, where X and Y are integers greater than one.
Create a function takes in an integer i and returns the (zero-indexed) ith power number

Write a function that returns the nth power number, where a power number is a number that can be expressed as x^y.
Note that the power number sequence is in ascending order (4, 8, 9, 16, 27, 32, ...).
"""

import time
import math

class Power_Checker:
    def __init__(self):
        self.dp = {}

    def is_power_number(self, n):
        # e.g. to check 10, 4^2 > 10 already so we know 4 can't be a base. Therefore the biggest base we need to check is
        # just floor(sqrt(n))
        biggest_possible_base = int(math.sqrt(n)) + 1

        for base in range(2, biggest_possible_base):
            power = 1
            check_ans = base

            while check_ans <= n:
                if check_ans == n:
                    # print('{}^{}'.format(base,power))
                    # print(self.dp)
                    return True

                if base in self.dp and power in self.dp[base]:
                    check_ans = self.dp[base][power]
                    # print('checked dp')
                else:
                    check_ans *= base
                    # print('multiplied')

                    if base not in self.dp:
                        self.dp[base] = {power:check_ans}
                    else:
                        self.dp[base][power] = check_ans

                power += 1

        return False


def nth_power_number(n):
    nth_power_number = n+1
    power_nums = [None] * nth_power_number
    sequential_num = 1
    checker = Power_Checker()

    for i in range(len(power_nums)):
        while not checker.is_power_number(sequential_num):
            sequential_num += 1

        power_nums[i] = sequential_num
        sequential_num += 1

    print(power_nums[-1])


start = time.time()
nth_power_number(200)
end = time.time()
print(end-start)

# for i in range(10):
#     print(is_power_number(i))

# print(is_power_number(4))
# print(is_power_number(8))
# print(Power_Checker().is_power_number(49))
# print(is_power_number(48))