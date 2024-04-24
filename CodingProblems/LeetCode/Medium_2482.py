import numpy as np

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        helper_rows = np.zeros((m, 2), dtype = int)
        helper_cols = np.zeros((n, 2), dtype = int)
        diff = np.zeros((m, n), dtype = int)
        grid = np.array(grid)
        for i in range(m):
            helper_rows[i][0] = len([1 for el in grid[i, :] if el == 1])
            helper_rows[i][1] = len([1 for el in grid[i, :] if el == 0])
        for i in range(n):
            helper_cols[i][0] = len([1 for el in grid[:, i] if el == 1])
            helper_cols[i][1] = len([1 for el in grid[:, i] if el == 0])
        for i in range(m):
            for j in range(n):
                diff[i][j] = helper_rows[i][0] + helper_cols[j][0] - helper_rows[i][1] - helper_cols[j][1]
        return diff
        