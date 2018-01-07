"""
"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis),
the output should be 79 (position of the last parenthesis).
"""

"""
Solution:
1) Uses a counter that starts at 1. Increment/decrement... if 0 we found it.
Time: O(n)    Space: O(1)
"""

def get_closing_index(arr,n):
    if arr[n] != '(':
        return -1

    counter = 1

    for i in range(n+1,len(arr)):
        if arr[i] == '(':
            counter += 1
        elif arr[i] == ')':
            counter -= 1
            if counter == 0:
                return i
    return -1

s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print(get_closing_index(s, 10))