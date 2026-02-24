
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        res = []
        for ele in nums1:
            res.append(next_greater[ele])

        return res