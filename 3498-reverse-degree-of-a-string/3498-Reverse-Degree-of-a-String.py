class Solution:
    def reverseDegree(self, s: str) -> int:
        ra=[]
        stt=[]
        ans=[]
        st="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(st)):
            ra.append(26-i)
            stt.append(st[i])
        for j in range(1,len(s)+1):
            k=stt.index(s[j-1])
            l=j*ra[k]
            ans.append(l)
        return sum(ans)