def fib_recursive(n):
    if n in [0, 1]:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

class Fibber:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in [0, 1]:
            return n

        if n in self.memo:                  # see if we've already calculated this
            return self.memo[n]
        result = self.fib(n - 1) + self.fib(n - 2)

        self.memo[n] = result               # memoize
        return result

def fib_dp(n, memo=None):
    if memo is None:
        memo = [0,1] + [None] * (n-1)

    if memo[n] is None:
        memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

def fib_2_variable(n):
    if n == 0 or n == 1:
        return n

    a = 0
    b = 1
    for n in range(n-1):
        tmp = b + a
        a = b
        b = tmp
    return b

# print(fib_recursive(90))
# print(Fibber().fib(8))
print(fib_dp(10))
print(fib_2_variable(10))