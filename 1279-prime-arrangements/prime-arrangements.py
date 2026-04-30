class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        p = sum(is_prime) 

   
        def fact(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res

       
        return (fact(p) * fact(n - p)) % MOD