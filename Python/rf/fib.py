def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    a=0
    b=1
    for i in range(0,n-1):
        tmp = b
        b=a+b
        a=tmp
    return b

print(fib(50))