def arrayMaxConsecutiveSum2(inputArray):
    dp_arr = [0] * len(inputArray)
    dp_arr[0] = inputArray[0]

    for i in range(1, len(inputArray)):
        # take it or take the previous
        dp_arr[i] = max(inputArray[i], inputArray[i] + dp_arr[i - 1])

    return max(dp_arr)

print(arrayMaxConsecutiveSum2())