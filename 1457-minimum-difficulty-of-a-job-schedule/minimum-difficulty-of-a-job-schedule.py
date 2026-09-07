from functools import lru_cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        @lru_cache(None)
        def dp(i, days_left):
            if i == n:
                if days_left == 0:
                    return 0
                else:
                    return float('inf')

            if days_left == 0:
                return float('inf')

            if n - i < days_left:
                return float('inf') 

            ans = float('inf')
            max_difficulty = 0

            for j in range(i,n):
                max_difficulty = max(max_difficulty,jobDifficulty[j])
                if n - (j + 1) < days_left - 1:
                    break

                ans = min(ans,max_difficulty + dp(j+1, days_left-1))
            return ans
        return dp(0,d)
