"""

xxx,xxx,xxx,xxx
b   m   t   ht

1,239,911
1,xxx,xxx   one million
2xx,xxx     two hundred thousand        --->    don't need to repeat "thousand"
3x,xxx      thirty thousand             --->
9,xxx       nine thousand               --->
9xx         nine hundred
1x          ten                         --->    NOT ten one, it's eleven (damn you english)
1           one                         --->

1,239,911   1,000,000       // 1,000,000 = 1
1,239,911   239,000         // 1,000 = 239
1,239,911   911

9325
9xxx    nine thousahd
3xx     three hundred
2x      twenty
5       five

351
3xx     three hundred
5x      fify
1       one

311
3xx     three hundred
1x      ten             --> NOT ten one, eleven...
1       one

"""

class Solution(object):
    def __init__(self):
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        i = 0
        words = ""

        while num > 0:
            remainder = num % 1000

            if remainder != 0:
                words = self.helper(remainder) + self.THOUSANDS[i] + " " + words

            num //= 1000
            i += 1

        return words.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.LESS_THAN_20[num] + " "
        elif num < 100:
            return self.TENS[num // 10] + " " + self.helper(num % 10)
        else:
            return self.LESS_THAN_20[num // 100] + " Hundred " + self.helper(num % 100)


print(Solution().numberToWords(1239991 ))