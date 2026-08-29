class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        ans = 0

        for i in range(len(digits)):
            if i % 2 == 0:
                ans += int(digits[i])
            else:
                ans -= int(digits[i])

        return ans