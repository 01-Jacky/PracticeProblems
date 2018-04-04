"""
Given and input string, generate an output string that count how many time each character appears consecutely in the string.
Ex input: aaabbacccddefa
Output: a3b2a1c2d2e1f1a1
"""

"""
aaabbacccddefa

cur_chr b
counter 1
aaab
a3
"""

def print_compressed_string(input_str):
    if len(input_str) < 1:
        return ""

    last_ch = input_str[0]
    counter = 0
    output_str = ""

    for cur_chr in input_str:
        if last_ch == cur_chr:
            counter += 1
        else:
            output_str = output_str + last_ch + str(counter)
            counter = 1
            last_ch = cur_chr

    if counter > 0:
        output_str = output_str + last_ch + str(counter)

    print(output_str)


print_compressed_string("aaabbacccddefa")
print_compressed_string("aaaaaa")
print_compressed_string("a8889###%aAaa")
print_compressed_string("")

