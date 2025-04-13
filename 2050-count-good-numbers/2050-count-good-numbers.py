class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 +7

        def calculate(x,y):
            result,multi=1,x
            while y > 0:
                if y % 2==1:
                    result=result * multi % mod
                multi=multi * multi % mod
                y//=2
            return result
        return calculate(5,(n+1)//2)*calculate(4,n//2) % mod
