# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def coinChange(coins, amount):
    """
    make 25
    10 5 2

    stack
    (10,[10]) removed
    (20,[10,10]) removed
    (15,[10,5])
    (12,[10,2])
    (25,[10,10,5]) FUCKING FOUND IT OMG
    """

    coins.sort(reverse=True)
    queue = collections.deque()

    # Let's put in the largest coin that fits
    for coin in coins:
        if coin <= amount:
            queue.append((coin,[coin]))
            break

    while queue:
        sum, coins_so_far = queue.popleft()

        if sum == amount:  # Goal check
            return coins_so_far

        # Add next squares to explore
        for coin in coins:
            if sum+coin <= amount:
                queue.append((sum+coin, coins_so_far + [coin]))

    return False, None

def coin_change(coins, withdraw, balance):
    if withdraw > balance:
        return "Cannot put into packets"

    print(coinChange(coins,withdraw))


    # But we gota print it this format:
    # amount:coin amount:coin  amount:coin
    # smallest to the left
    ratio_lst = []
    for coin, amount in sorted(ratio.items()):
        ratio_lst.append('{}:{}'.format(amount, coin))
    coin_ratios = ' '.join(ratio_lst)

    return coin_ratios + ' ' + str(balance - withdraw_request)


# Prep inputs
line1 = input()
balance, withdraw, coins_to_read = line1.split(" ")
balance = int(balance)
withdraw = int(withdraw)
coins_to_read = int(coins_to_read)
coins = [int(input()) for i in range(coins_to_read)]

print(coin_change(coins, withdraw, balance))