
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        # Step 1: Count frequency
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        # Step 2: Find first unique character
        for i, ch in enumerate(s):
            if hashmap[ch] == 1:
                return i

        return -1