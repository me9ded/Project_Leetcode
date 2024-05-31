class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start=0
        res=0
        answer=0
        for i in range(len(s)):
            res+=abs(ord(s[i])-ord(t[i]))
            while res > maxCost:
                res-=abs(ord(s[start])-ord(t[start]))
                start+=1
            answer=max(answer,i-start+1)
        return answer