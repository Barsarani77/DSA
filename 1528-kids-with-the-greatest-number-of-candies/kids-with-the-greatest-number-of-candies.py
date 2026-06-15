class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        result = []

        for candy in candies:
           if  candy + extraCandies >= largest:
            result.append(True)
           else:
            result.append(False)
        return result