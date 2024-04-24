from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        start, end = 0, row * col
        while start < end:
            half = start + (end - start) // 2
            if matrix[half // col][half % col] == target:
                return True
            elif matrix[half // col][half % col] > target:
                end = half
            else:
                start = half + 1
        return False
    
print(Solution().searchMatrix([[1,1]], 0))