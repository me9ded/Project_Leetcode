class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        if k==1:
            return max(happiness)
        happiness=sorted(happiness,reverse=True)
        res=happiness[:k]
        for i in range(1,len(res)):
            res[i]-=i
            if res[i]<0:
                res[i]=0
        print(res)
        return sum(res)

        



