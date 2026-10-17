class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr=[]
        co=0
        q=0
        for i in nums:
            k=str(i)
            su=0
            for l in k:
                su=su+int(l)
            arr.append(su)
        for i in range(len(arr)):
            print(arr)
            p=min(arr)
            if(p!=arr[0]):
                if(p==q):
                    if(i!=len(arr)):
                        if(arr[i]>=arr[i+1]):
                            co=co+1
                else:
                    co=co+1
            q=p
            arr.remove(p)
            
        return co
