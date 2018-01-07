class Solution(object):
    # Solution 1
    # Time: O(n^2)  Space: O(n)
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_row_letter_sets = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []

        for word in words:
            letter_set = set(word.lower())
            for row_set in keyboard_row_letter_sets:
                if letter_set.issubset(row_set):
                    res.append(word)
                    continue
        return res

    # Solution 2
    # def findWords(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: List[str]
    #     """
    #     return [word for word in words if self.is_onerow_possible(word)]
    #
    # def is_onerow_possible(self, word):
    #     ROWS = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    #     a = 0
    #     b = 0
    #     c = 0
    #
    #     for ch in word.lower():
    #         if ch in ROWS[0]:
    #             a += 1
    #         elif ch in ROWS[1]:
    #             b += 1
    #         elif ch in ROWS[2]:
    #             c += 1
    #
    #         if a > 0 and (b != 0 or c != 0):
    #             return False
    #         if b > 0 and (a != 0 or c != 0):
    #             return False
    #         if c > 0 and (a != 0 or b != 0):
    #             return False
    #     return True


print(Solution().findWords(['Hello', 'Alaska']))
