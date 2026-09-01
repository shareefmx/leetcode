class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        arr = sorted(cost, reverse=True)
        print(arr)
        su=0
        for i in range(len(arr)):
            if((i+1)%3!=0):
                su=su+arr[i]
        return su