"""
cats
1023

base 4

4^3 * 1 = 64
4^2 * 0 = 0
4^1 * 2 = 8
4^0 * 3 = 3

11001001
11001001

"""

def _get_min_value(input):
    ORDER = ['1','0','2','3','4','5','6','7','8','9']
    cur_index = 0
    mapping = {}
    min_value_string = ''

    for ch in input:
        if ch in mapping:
            min_value_string += mapping[ch]
        else:
            mapping[ch] = ORDER[cur_index]
            min_value_string += ORDER[cur_index]
            cur_index += 1

    return min_value_string, cur_index     # cur_index is also the min base

def _get_base_10(input, base):
    cur_pow = 0
    sum = 0

    for ch in input[::-1]:
        cur_value = (base**cur_pow) * int(ch)
        sum += cur_value
        cur_pow += 1

    return sum

def decodeInput(input):
    # min_value_string, min_base = _get_min_value(input)
    # return _get_base_10(min_value_string, min_base)

    min_value_string, min_base = _get_min_value(input)

    # CONVERT BASE 10
    cur_pow = 0
    sum = 0

    for ch in min_value_string[::-1]:
        cur_value = (min_base**cur_pow) * int(ch)
        sum += cur_value
        cur_pow += 1

    return sum

# print(_get_min_value('cats'))
# print(_get_min_value('11001001'))

# print(_get_base_10('11001001',2))
# print(_get_base_10('1023',4))


print(decodeInput('cats'))
print(decodeInput('11001001'))
print(decodeInput('zig'))
