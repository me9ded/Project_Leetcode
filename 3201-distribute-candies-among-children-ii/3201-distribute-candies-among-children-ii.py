class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result=0
        for i in range(min(limit,n)+1):
            if n-i > 2*limit:
                continue
            result+=min(limit,n-i)-max(0,n-i-limit)+1
        return result