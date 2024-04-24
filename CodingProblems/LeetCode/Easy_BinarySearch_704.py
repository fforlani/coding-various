from typing import List

class SolutionRecursive:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        half = len(nums) // 2
        if nums[half] > target:
            return self.search(nums[:half], target)
        else:
            value = self.search(nums[half:], target)
            return -1 if value == -1 else half + value
        
class SolutionIterative:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            half = start + (end - start) // 2
            if nums[half] == target:
                return half
            elif nums[half] > target:
                end = half
            else:
                start = half + 1
        return -1


print(SolutionRecursive().search([-1,0,3,5,9,12], 9))
print(SolutionIterative().search([-1,0,3,5,9,12], 9))
