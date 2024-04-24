from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        for num in nums:
            for i in range(len(arr)):
                arr.append(arr[i] + [num])
        return arr
    
sol = Solution().subsets(nums = [1, 2, 3])
print(sol)