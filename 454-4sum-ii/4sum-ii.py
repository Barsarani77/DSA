class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        from collections import defaultdict
        
        count_map = defaultdict(int)
        
      
        for a in nums1:
            for b in nums2:
                count_map[a + b] += 1
        
        result = 0
        
       
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count_map:
                    result += count_map[target]
        
        return result