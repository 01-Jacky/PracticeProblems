"""
We want to find the most popular base choice.
The most popular base choice is defined as a combination of different food items, including 1 additional item.
For example, if you have orders for
"pizza, hamburger",
"pizza hamburger",
"pizza hamburger soda",
"pizza hamburger fries",

the total count for "pizza hamburger" food choice would be 4. 
So design an algorithm find the most popular food base choice, and describe its time complexity.  

-----

Solutions:
1) For each order, get combinations and track it's frequency

(hamburger, pizza) -> 4
(pizza, soda) -> 1
...

max freq so far = 4
max combo = (hamburger, pizza)

o = orders
f =
Time: O(o*(f^2)) Space: O(f)

"""


def get_combination(string):
    combinations = []
    for i in range(len(string)):
        for ch in string[i+1:]:
            if string[i] > ch:
                combinations.append((ch, string[i]))
            else:
                combinations.append((string[i], ch))

    return combinations

def most_common_combo(strings):
    freq = {}

    max_freq = 0
    max_freq_combo = None

    for string in strings:
        for combination in get_combination(string):
            # Record the combination into our freq table
            if combination in freq:
                freq[combination] += 1

                # Update best answer as we go along... or omit this and iterate through the freq table at the end
                if freq[combination] > max_freq:
                    max_freq = freq[combination]
                    max_freq_combo = combination
            else:
                freq[combination] = 0
    return max_freq_combo

# 'ac' is the most common combination
strings = [
    'abcd',
    'abcd',
    'ad',
    'acde',
    'cb'
]

print(get_combination('abcd'))
print(most_common_combo(strings))