from collections import defaultdict

class Solution:
    def maxOperations(self, nums, k):
        count = defaultdict(int)
        ans = 0

        for num in nums:
            need = k - num

            if count[need] > 0:
                ans += 1
                count[need] -= 1
            else:
                count[num] += 1

        return ans