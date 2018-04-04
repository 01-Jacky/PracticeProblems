"""
Print nth Fib

1) Recursion
Time O(2^n) Space O(n)

2) Recursion + Mem
Time O(n) Space O(n)

3) Bottom up DP
Time O(n) Space O(1)
"""

# 1
def fib_recursion(n):
    if n in [0,1]:
        return n
    return fib_recursion(n-1) + fib_recursion(n-2)


# 2
def fib_recursion_mem(n):
    mem = [None] * (n+1)
    mem[0] = 0
    mem[1] = 1
    return _fib_recursion_mem_helper(n, mem)


def _fib_recursion_mem_helper(n, mem):
    if mem[n] is not None:
        return mem[n]
    else:
        nth_fib = _fib_recursion_mem_helper(n-1,mem) + _fib_recursion_mem_helper(n-2,mem)
        mem[n] = nth_fib
        return mem[n]

# 2 alternative
class Fibber:
    def __init__(self, n):
        self.mem = {}
        self.mem[0] = 0
        self.mem[1] = 1

    def fib(self, n):
        if self.self.mem[n] is not None:
            return self.mem[n]
        else:
            nth_fib = self.fib(n - 1, self.mem) + self.fib(n - 2, self.mem)
            self.mem[n] = nth_fib
            return self.mem[n]


print(fib_recursion(7))
print(fib_recursion_mem(5))