from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        rd = sorted(zip(robots, distance))
        n = len(rd)

        def cnt(a, b):
            if a > b:
                return 0
            return bisect_right(walls, b) - bisect_left(walls, a)

        left = right = 0
        prev_R = 0
        for i, (r, d) in enumerate(rd):
            L = r - d
            if i > 0:
                L = max(L, rd[i - 1][0] + 1)
            R = r + d
            if i + 1 < n:
                R = min(R, rd[i + 1][0] - 1)

            if i == 0:
                new_left = cnt(L, r)
                new_right = cnt(r, R)
            else:
                new_left = max(left, right - cnt(L, prev_R)) + cnt(L, r)
                new_right = max(left, right) + cnt(r, R)

            left, right = new_left, new_right
            prev_R = R

        return max(left, right)