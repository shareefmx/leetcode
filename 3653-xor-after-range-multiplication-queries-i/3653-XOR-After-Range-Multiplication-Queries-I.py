class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        res = 0
        for x in nums:
            res ^= x
        return res