class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            su=0
            st=str(nums[i])
            for k in st:
                su=su+int(k)
            if(su==i):
                arr.append(su)
        if(len(arr)!=0):
            return min(arr)
        else:
            return -1