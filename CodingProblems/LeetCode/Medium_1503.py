from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            left = [0]
        if not right:
            right = [n]
        return max(max(left), n - min(right))