class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=[]
        odd=0
        count=Counter(s)
        for num in count.values():
            res.append(num)
            if num%2!=0:
                odd+=1
        if odd!=0:
            return sum(res)-odd+1
        else:
            return sum(res)-odd
        