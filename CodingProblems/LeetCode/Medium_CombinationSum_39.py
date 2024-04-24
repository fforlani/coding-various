from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return []
        if target < 0:
            return None
        ret = []
        for candidate in candidates:
            ric = self.combinationSum(candidates[candidates.index(candidate):], target - candidate)
            if ric is not None:
                if len(ric) == 0:
                    ret += [[candidate]]
                else:
                    ret += [[candidate] + sub for sub in ric]
        return None if len(ret) == 0 else ret