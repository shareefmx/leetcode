class Solution:
    def maxDepth(self, s: str) -> int:
        co=0
        ar=[]
        for i in s:
            if(i=="("):
                co=co+1
                ar.append(co)
            elif(i==")"):
                co=co-1
                ar.append(co)
        return 0 if len(ar) == 0 else max(ar)
