class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result=0
        for i in range(low,high+1):
            if i % 2 !=0:
                result+=1
        return result