class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        # Handle negative numbers (32-bit)
        num &= 0xffffffff
        
        while num > 0:
            digit = num & 15   # last 4 bits
            result = hex_chars[digit] + result
            num >>= 4
        
        return result