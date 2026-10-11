class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        su=0
        n=len(nums)
        for i in range(len(nums)):
            if(n%(i+1)==0):
                su=su+(nums[i]*nums[i])
        return su