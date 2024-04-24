from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        start, end = 0, l
        while start < end:
            half = start + (end - start) // 2
            if half + 1 == l:
                if nums[l -2] > nums[l - 1]:
                    return nums[l - 1]
                else:
                    return nums[0]
            if nums[half] > nums[half + 1]:
                return nums[half + 1]
            elif nums[half] < nums[0]:
                end = half
            else:
                start = half + 1
        return None
    
print(Solution().findMin([2,3,4,5,1]))