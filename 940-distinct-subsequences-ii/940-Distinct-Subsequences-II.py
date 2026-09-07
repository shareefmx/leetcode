from itertools import combinations

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        arr=[]
        for r in range(1, len(s) + 1):
            for c in combinations(s, r):
                k="".join(c)
                arr.append(k)
        return len(set(arr))

