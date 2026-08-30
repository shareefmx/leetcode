class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        from_front = right + 1
        from_back = n - left
        both_sides = (left + 1) + (n - right)

        return min(from_front, from_back, both_sides)