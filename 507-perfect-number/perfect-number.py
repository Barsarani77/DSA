class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        n = num
        total = 1
        
        p = 2
        while p * p <= n:
            if n % p == 0:
                curr_sum = 1
                curr_term = 1
                while n % p == 0:
                    n //= p
                    curr_term *= p
                    curr_sum += curr_term
                total *= curr_sum
            p += 1
        
        if n > 1:
            total *= (1 + n)
        
        return total - num == num