# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_printout(min_coins):
    freq_map = {}
    for coin in min_coins:
        if coin in freq_map:
            freq_map[coin] += 1
        else:
            freq_map[coin] = 1

    ratios = []
    for coin, freq in sorted(freq_map.items()):
        ratios.append('{}:{}'.format(freq, coin))

    return ' '.join(ratios)


def print_coin_change(coins, amount, balance):
    coins.sort()
    dp = [float('inf')] * (amount + 1)
    seq = [0] * (amount + 1)
    dp[0] = 0

    # Build solution
    for i in range(amount + 1):
        for j in range(len(coins)):
            cur_coin_amount = coins[j]
            if cur_coin_amount <= i:
                dp[i] = 1 + dp[i - coins[j]]
                seq[i] = j

    # Find path
    if dp[-1] == float('inf'):
        print("Cannot put into packets")
    else:
        min_coins = []
        j = amount
        while j:
            best_coin_at_amount = coins[seq[j]]
            min_coins.append(best_coin_at_amount)
            j = j - coins[seq[j]]

        ratios_str = get_printout(min_coins)
        print(ratios_str + ' ' + str(balance - amount))


# Prep inputs
line1 = input()
balance, withdraw, coins_to_read = line1.split(" ")
balance = int(balance)
withdraw = int(withdraw)
coins_to_read = int(coins_to_read)
coins = [int(input()) for i in range(coins_to_read)]

print_coin_change(coins, withdraw, balance)