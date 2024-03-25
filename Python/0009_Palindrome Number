class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        res=str(x)
        l,r=0,len(res)-1
        while l<=r:
            if res[l]!=res[r]:
                return False
            else:
                l+=1
                r-=1
        return True