class Solution:
    def minSwaps(self, s: str) -> int:
        temp=0
        res=0
        for c in s:
            temp+= c=='['
            temp-= c==']'
            if temp < 0:
                temp=1
                res+=1
        return res

        