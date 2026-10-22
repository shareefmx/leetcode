from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        for k in range(n):
            rotated = nums[k:] + nums[:k]

            if rotated == list(range(n)):
                return k

            reversed_rotated = rotated[::-1]

            if reversed_rotated == list(range(n)):
                return k + 1

        return -1