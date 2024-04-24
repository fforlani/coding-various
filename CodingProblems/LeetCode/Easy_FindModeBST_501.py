# Definition for a binary tree node.
from functools import reduce
from typing import List, Optional, Tuple

from collections import Counter
from operator import add

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### EASY WAY ###
class SolutionEasy:
    def __init__(self):
        self.nums = {}

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        m = max(self.nums.values())
        return [key for key in self.nums if self.nums[key] == m]
        
    def helper(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        if root.val in self.nums.keys():
            self.nums[root.val] += 1
        else:
            self.nums[root.val] = 1
        self.helper(root.left)
        self.helper(root.right)

### EFFICIENT SOLUTION ###
#This solution is not accepted by LeetCode, because obviously fail on a tree which is not a BST
class Solution:   

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        return Solution.getMaxKeys(self.modeWithCount(root))
    
    def modeWithCount(self, root: Optional[TreeNode]) -> dict[int, int]:
        if root is None:
            return {}
        leftMode = self.modeWithCount(root.left)
        rightMode = self.modeWithCount(root.right)
        modes = sum((Counter(dict(x)) for x in [leftMode, rightMode]), Counter())
        if not modes:
            return {root.val : 1}
        print(leftMode, rightMode, modes)
        nums = Solution.getMaxKeys(modes)
        if root.val in modes.keys():
            if root.val in nums:
                return {root.val : modes[root.val] + 1}
            else:
                return {root.val : modes[root.val] + 1} | {num : modes[nums[0]] for num in nums}
        else:
            return {root.val : 1} | {num : modes[nums[0]] for num in nums}

    def getMaxKeys(dic: dict[int, int]) -> List[int]:
        m = max(dic.values())
        return [key for key in dic if dic[key] == m]
