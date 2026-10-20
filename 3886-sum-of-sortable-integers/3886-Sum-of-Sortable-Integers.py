class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            prev = 0
            ok = True
            for s in range(0, n, k):
                b = nums[s:s + k]
                d = [i for i in range(k - 1) if b[i] > b[i + 1]]
                if len(d) > 1 or (d and b[-1] > b[0]):
                    ok = False
                    break
                if d:
                    lo, hi = b[d[0] + 1], b[d[0]]
                else:
                    lo, hi = b[0], b[-1]
                if lo < prev:
                    ok = False
                    break
                prev = hi
            if ok:
                ans += k
        return ans