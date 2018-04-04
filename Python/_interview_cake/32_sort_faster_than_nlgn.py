"""
unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# returns [91, 89, 65, 53, 41, 37]

Do this faster than n log n
"""

def sort_score(scores, HIGHEST_POSSIBLE_SCORE):
    # Construct the frequency table
    freq_table = [0] * (HIGHEST_POSSIBLE_SCORE+1)
    for score in scores:
        freq_table[score] += 1

    # Walk through the table
    ans = []
    for score in range(len(freq_table)-1, -1, -1):
        for frequency in range(freq_table[score]):      # e.g. [0, 3, 2, 0 ,1] means 3 instance of score = 1
            ans.append(score)

    return ans

print(sort_score([37, 89, 41, 65, 91, 53, 89], 100))