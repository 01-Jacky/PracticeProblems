def print_matrix(coin, dp):
    lst = [str(i) for i in range(len(dp[0]))]
    print('    ' + '  '.join(lst))

    for i, row in enumerate(dp):
        lst = [str(el).rjust(2,' ') for el in row]
        # print(lst)
        print(str(coin[i]) + "| "+ " ".join(lst))
    print()

def coinChange(coins, total):
    n = len(coins)
    dp = []
    for i in range(n):
        dp.append([0 for i in range(total+1)])

    # for i in range(1,total+1):
    #     dp[0][i] = i

    for i in range(1,amount+1):
        if i % coins[0] == 0:
            dp[0][i] = i//coins[0]

    # print_matrix(coins, dp)

    for i in range(1, n):
        for j in range(1, total+1):
            _i = i
            _j = j
            if coins[i] > j:    # if denom is greater than total
                dp[i][j] = dp[i-1][j]
            else:               # if denom is less than or equal total
                up = dp[i-1][j]
                left = 1 + dp[i][j-coins[i]]
                if min(up, left) == 0 and j % coins[i] == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i]])

    print_matrix(coins, dp)
    return dp[n-1][total], dp

def printChange(coins, dp, total):
    i = len(coins) - 1
    j = total
    min = dp[i][j]
    ans = []

    while j != 0:
        if dp[i-1][j] == min:
            i = i - 1
        else:
            ans.append(coins[i])
            j = j - coins[i]
            min = dp[i][j]

    return ans

coins = [1,5,6,8]
amount = 11

coins = [2,5]
amount = 10

coins = [2,5,10,50,100]
amount = 12

min_coin, dp = coinChange(coins, amount)
print(min_coin)
# print(printChange(coins, dp, amount))

