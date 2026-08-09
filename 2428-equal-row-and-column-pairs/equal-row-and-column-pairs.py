from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}

        
        for row in grid:
            row = tuple(row)
            rows[row] = rows.get(row, 0) + 1

        count = 0

        
        n = len(grid)

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))

            if col in rows:
                count += rows[col]

        return count