class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set(nums)

        for i in range(2 ** n):
            s = format(i, f'0{n}b')

            if s not in seen:
                return s   