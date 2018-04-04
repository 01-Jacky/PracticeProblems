#!/usr/bin/python

import sys


def minimum_coins_change(denominations, value):
    result = None

    if value == 0:
        result = {}
        for denom in denominations:
            result[denom] = 0
    elif len(denominations) == 0:
        result = None
    else:
        denom = denominations[0]
        rest = denominations[1:]
        rest_result = {}

        max_count = value // denom
        min_coin_count = float('inf')

        for i in range(max_count + 1):
            current_value = value - (denom * i)
            rest_result = minimum_coins_change(rest, current_value)
            # if we can make change given the remainder

            if rest_result != None:
                new_count = i + sum(rest_result.values())
                # test to see if this new set is the minimum coin count
                if new_count < min_coin_count:
                    # if so, set it to our result
                    min_coin_count = new_count
                    result = rest_result
                    result[denom] = i
    return result


def print_result(denominations, value, result):
    print("Smallest change for", value, "using denominations:", denominations)
    if result == None:
        print("  No change possible")
    else:
        print("  %d coins needed" % sum(result.values()))
        print("  distributed via", sorted(result.items()))
    print()


denominations = [1, 5, 10, 50, 100]
value = 567
result = minimum_coins_change(denominations, value)
print_result(denominations, value, result)

# denominations = [1]
# value = 67
# result = minimum_coins_change(denominations, value)
# print_result(denominations, value, result)
#
# denominations = [5]
# value = 69
# result = minimum_coins_change(denominations, value)
# print_result(denominations, value, result)
#
# denominations = [5, 1]
# value = 43
# result = minimum_coins_change(denominations, value)
# print_result(denominations, value, result)
#
# denominations = [100, 50, 25, 10, 5, 1]
# value = 72
# result = minimum_coins_change(denominations, value)
# print_result(denominations, value, result)
#
# denominations = [67, 42, 34, 15, 8]
# value = 124
# result = minimum_coins_change(denominations, value)
# print_result(denominations, value, result)
