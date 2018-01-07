def foo(num):
    if num <= 0:
        return False
    for x in [5,3,2]:
        while num % x == 0:
            num = num / x
    return num == 1


print(foo(8))