class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        k = len(sq) // 2         
        return sum(sq[k:]) - sum(sq[:k])