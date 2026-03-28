class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        def is_self_dividing(num):
            for d in str(num):
                digit = int(d)
                if digit == 0 or num % digit != 0:
                    return False
            return True
        
        result = []
        
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
        
        return result