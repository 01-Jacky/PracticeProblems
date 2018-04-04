"""
1)
99
 ^ carry
90
^ carry
00


"""

class Solution(object):
    def plusOne(self, digits):
        # init the problem by adding 1 to the first digit
        digits[-1] += 1
        carry = 0
        if digits[-1] < 10:
            return digits
        else:
            digits[-1] = 0
            carry = 1

        # See how far we need to carry
        for i in range(len(digits)-2,-1,-1):
            cur_digit = digits[i] + carry

            if cur_digit < 10:
                digits[i] = cur_digit
                return digits
            else:
                carry = 1
                digits[i] = 0

        # If there's a carry we need a new array
        return [1] + digits if carry else digits

print(Solution().plusOne([1,0]))
print(Solution().plusOne([9]))
print(Solution().plusOne([9,9]))
print(Solution().plusOne([8,9,9]))
print(Solution().plusOne([5,8,7,8,8]))
