"""
  def number_of_ways(amount, denominations):
    answer = 0
    for each denomination in denominations:
        for each num_times_to_use_denomination in possible_num_times_to_use_denomination_without_overshooting_amount:
            answer += number_of_ways(amount_remaining, other_denominations)
    return answer
"""

def change_possibilities_top_down(amount_left, denominations, current_index=0):
    if amount_left == 0:
        return 1
    if amount_left < 0:
        return 0
    if current_index == len(denominations):
        return 0

    print("checking ways to make %i with %s" % (amount_left, denominations[current_index:]))
    current_coin = denominations[current_index]

    # see how many possibilities we can get for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left, denominations, current_index + 1)
        amount_left -= current_coin
    return num_possibilities


# This is like the one before but add a memorization
def change_possible_dp(amount_left, denominations, current_index=0, memo={}):
    key = str((amount_left, current_index))
    if key in memo:
        print('grab memo {}'.format(key))
        return memo[key]

    if amount_left == 0:
        return 1
    if amount_left < 0:
        return 0
    if current_index == len(denominations):
        return 0

    print("checking ways to make %i with %s" % (amount_left, denominations[current_index:]))
    current_coin = denominations[current_index]

    # see how many possibilities we can get for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possible_dp(amount_left, denominations, current_index + 1, memo)
        amount_left -= current_coin
    memo[key] = num_possibilities
    return num_possibilities

def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        print('coin {}, way= {}'.format(coin,ways_of_doing_n_cents))
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
            print(ways_of_doing_n_cents)

    return ways_of_doing_n_cents[amount]

# print(change_possibilities_top_down(4, [1, 2, 3]))
# print(change_possible_dp(4, [1, 2, 3]))
# print(change_possibilities_bottom_up(4, [1, 2, 3]))
print(change_possibilities_bottom_up(15, [1, 3, 5]))

