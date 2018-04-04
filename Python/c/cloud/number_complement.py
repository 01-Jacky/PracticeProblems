def getIntegerComplement(n):
    binary_string = "{0:b}".format(n)
    complement_string = ''.join(['1' if bit == '0' else '0' for bit in binary_string])
    return int(complement_string, 2)    # 2 for bianry number

print(getIntegerComplement(50))