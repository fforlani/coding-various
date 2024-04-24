from functools import cmp_to_key
import numpy as np
from typing import List

class Solution:
    def __init__(self):
        self.cur_best = 0
        self.best_end = None #best_end[i] = best count found of jobs which end at time i or before

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def isValid(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return True
            return startTime[order[i]] >= endTime[order[j]] or startTime[order[j]] >= endTime[order[i]]

        def compare(i: int, j: int) -> bool:
            return startTime[i] - startTime[j]
            
        n = len(startTime)
        self.best_end = np.zeros(max(endTime) + 1, dtype = int)
        order = sorted(range(n), key=cmp_to_key(compare))
        def checkRec(curJob: int, curCount: int):
            if curCount < self.best_end[endTime[order[curJob]]]:
                return
            for i in range(curJob + 1, n):
                if isValid(curJob, i):
                    if curCount + profit[order[i]] > self.best_end[endTime[order[i]]]:
                        self.best_end[endTime[order[i]]:] = curCount + profit[order[i]]
                        checkRec(i, curCount + profit[order[i]])
            self.cur_best = max(self.cur_best, curCount)

        checkRec(-1, 0)
        print(self.best_end)
        return self.cur_best