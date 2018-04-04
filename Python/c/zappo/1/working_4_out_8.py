# Enter your code here. Read input from STDIN. Print output to STDOUT

def coin_change(coins, withdraw, balance):
    if withdraw > balance:
        return "Cannot put into packets"

    coins.sort(reverse=True)  # Make sure we build up from smallest denom to largest
    withdraw_request = withdraw

    # Try greedy to get the ratio of coin:amount.
    # This won't work for ALL currency system. US currency this is okay but some other ones may not.
    # e.g. make 9 out of coins 5 and 3. There's no solution with 5 but you can surely do 3,3,3.
    # Some failed test cases may be due tot his

    # I tried a DP solution but that used too much memory and caused memory error in hackerank
    # Could probably also use a BFS approach but I'm out of time
    ratio = {}
    for coin in coins:
        num_of_coins = withdraw // coin
        if num_of_coins > 0:
            ratio[coin] = num_of_coins
            withdraw -= coin * num_of_coins

    if withdraw > 0:
        return "Cannot put into packets"

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