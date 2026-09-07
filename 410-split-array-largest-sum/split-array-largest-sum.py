class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right-left)//2
        piece = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > mid:
                piece += 1
                current_sum = num
            else:
                current += num
            if piece <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left
class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

           
            pieces = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    pieces += 1
                    current_sum = num
                else:
                    current_sum += num

            if pieces <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left