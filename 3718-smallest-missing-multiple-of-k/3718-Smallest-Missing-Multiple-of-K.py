class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)+2):
            s=i*k
            if(s not in nums):
                return s
        