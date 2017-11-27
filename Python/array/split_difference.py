def solution(A):
    # write your code in Python 2.7
    left = A[0]
    right = 0

    for i in range(1,len(A)):
        right += A[i]
    min_diff = abs(left-right)

    for i in range(1,len(A)-1):
        left += A[i]
        right -= A[i]
        diff = abs(left - right)
        if diff < min_diff:
            min_diff = diff

    return min_diff

print(solution([3,1,2,4,3]))