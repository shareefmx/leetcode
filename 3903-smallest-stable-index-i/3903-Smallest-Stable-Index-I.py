class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            o = max(nums[:i + 1])
            p = min(nums[i:])
            su = o - p

            if su <= k:
                return i

        return -1