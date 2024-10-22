class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen=set()
        return self.backtrack(s,0,seen)
    def backtrack(self,s,start,seen):
        if start==len(s):
            return 0
        res=0
        for end in range(start+1,len(s)+1):
            string=s[start:end]
            if string not in seen:
                seen.add(string)
                res=max(res,1+self.backtrack(s,end,seen))
                seen.remove(string)
        return res
        