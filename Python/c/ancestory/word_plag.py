"""
Design and implement the analyzer module of a (very simple) plagiarism-detection service (like TurnItIn.com).
The module needs to output the % of matches between the two texts. Ignore matches of less than 4 words.
 
Example Input:
text1:
The quick brown fox jumps over the lazy dog
 
text2:
The lazy dog barks at the quick brown fox
 
Output:
- 44% (4 out of 9 words in text1 are found in text2)
 
Constraints:
- Input will always be less than 100000 characters.
"""

"""
The quick brown fox jumps over the lazy dog
The quick brown fox
"""