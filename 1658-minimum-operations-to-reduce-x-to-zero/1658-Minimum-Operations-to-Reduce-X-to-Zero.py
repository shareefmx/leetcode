class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        left = 0
        window_sum = 0
        best = -1
        
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                best = max(best, right - left + 1)
        
        return len(nums) - best if best != -1 else -1