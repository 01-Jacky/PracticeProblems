def solution(A):
    # write your code in Python 2.7
    bag = set()
    for i in A:
        if i in bag:
            bag.remove(i)
        else:
            bag.add(i)
    return bag.pop()

def solution2(A):
    # write your code in Python 2.7
    result = 0
    for i in A:
        result ^= i
    return result

A=[9, 3, 9, 3, 9, 7, 9]
print(solution2(A))





