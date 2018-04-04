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

def coin_change(coins, amount, balance):
    coins.sort()    # Make sure we build up from smallest denom to largest
    dp = [float('inf')] * (amount + 1)
    seq = [0] * (amount + 1)
    dp[0] = 0

    for i in range(amount + 1):
        for j in range(len(coins)):
            cur_coin_amount = coins[j]
            if cur_coin_amount <= i:                       #and dp[i - coins[j]] < dp[i]
                # dp[i] = min(dp[i], 1 + dp[i - cur_coin_amount])
                dp[i] = 1 + dp[i - coins[j]]    # don't need to do min because if another coin work, still using min coins
                seq[i] = j                      # j is the index of the best coin to use
            # print(dp)

    # print(dp)
    # print(seq)

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

        print(ratios_str + ' ' + str(balance-amount))


# line1 = input()
# balance, withdraw, coins_to_read = line1.split(" ")
# balance = int(balance)
# withdraw = int(withdraw)
# coins_to_read = int(coins_to_read)
#
# coins = [None] * coins_to_read
# for i in range(coins_to_read):
#     coins[i] = int(input())


# coins = [2,5,10,50,100]
# amount = 567

# coins = [500]
# amount = 567
#
# coins = [2,5,10]
# amount = 17

coins = [5,2,3,1]
withdraw = 6
balance = 100

coin_change(coins, withdraw, balance)