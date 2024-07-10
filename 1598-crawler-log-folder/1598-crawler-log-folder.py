class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        for char in logs:
            if char=="../":
                res=max(0,res-1)
            elif char!="./":
                res+=1
        return res
        