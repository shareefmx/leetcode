import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        arr=[]
        st=str(n)
        for i in st:
            arr.append(int(i))
        su=sum(arr)+math.prod(arr)
        print(su)
        if(n%su==0):
            return True
        else:
            return False
        