def convertTo7(num_based_n, n):
    if num == 0: return '0'
        n, res = abs(num), ''
    while n:
      res = str(n % 7) + res
      n //= 7
    return res if num > 0 else '-' + res

