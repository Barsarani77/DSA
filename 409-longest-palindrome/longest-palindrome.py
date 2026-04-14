class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        length = 0
        
        for ch in s:
            if ch in char_set:
                char_set.remove(ch)
                length += 2
            else:
                char_set.add(ch)
        
        
        if char_set:
            length += 1
        
        return length       