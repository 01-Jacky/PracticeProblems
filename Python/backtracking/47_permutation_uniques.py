class Perm():
    def __init__(self, nums):
        self.nums = nums

    def __hash__(self):
        hash = 1
        for i in enumerate(self.nums):
            hash =
        hash = hash * 17 + employeeId;
        hash = hash * 31 + name.hashCode();
        hash = hash * 13 + (dept == null ? 0 : dept.hashCode());
        return hash(self.__key())

    def __repr__(self):
        return str(self.nums)

class Solution(object):

    def _get_inserted_values(self, s, c_to_insert, i_max):
        """ Generate list of possible strings by inserting c in each possible from i to i_max"""
        res = []
        for i in range(i_max + 1):
            char_arr = list(s)
            char_arr.insert(i, c_to_insert)
            res.append(char_arr)
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        Idea: Start answer (list of perms) as 1 string with the first char.
        For the next character, take each element in ans and get the perms
        generated from it (by inserting it in each possible place).
        Given [1,2,3]
        [1]
        [21] [12] <--- take [1] and insert 2 into all possible indexes 0, 1 (e.g. [_1] [1_])
        [321] [231] [213] [312] [132] [123] <--- take [21] and insert 3 in each possible place. Do same for [12]
        etc.

        Time:   O(n^3)?
        Space:  O(n)
        """
        s = nums
        if len(s) <= 1:
            return [s]

        ans = [[s[0]]]  # Initialize with 1st char e.g. ans = [1]
        for i in range(1, len(s)):  # For rest of chars, insert into all possible places from existing ans
            tmp_ans = []
            # print('inserting {} into indexes 0 to i={}'.format(s[i],i))

            for e in ans:
                perm_of_e = self._get_inserted_values(e, s[i], i)
                tmp_ans.extend(perm_of_e)
            # print(tmp_ans)
            ans = tmp_ans

        uniques = set()
        for perm in ans:
            uniques.add(Perm(perm))
        print(uniques)

        # return [[int(float(c)) for c in s] for s in uniques]

print(Solution().permute([1,1,2]))
