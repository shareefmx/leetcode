class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [None] * n  

        for i in range(m):
            cur = [None] * n
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    cur[j] = {v}
                    continue
                src = set()
                if i > 0:
                    src |= prev[j]
                if j > 0:
                    src |= cur[j - 1]
                cur[j] = {x ^ v for x in src}
            prev = cur

        return min(prev[n - 1])