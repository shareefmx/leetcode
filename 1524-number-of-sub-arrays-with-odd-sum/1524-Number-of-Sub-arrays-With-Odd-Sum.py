class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ap=[]
        co=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                ap.append(arr[j])
                if(sum(ap)%2!=0):
                    co=co+1
            ap=[]
        return co