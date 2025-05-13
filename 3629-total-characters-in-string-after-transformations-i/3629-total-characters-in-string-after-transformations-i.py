class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        f=[0]*26

        for ch in s:
            f[ord(ch)-ord("a")]+=1

        for _ in range(t):
            temp=[0]*26
            temp[0]=f[25]
            temp[1]=(f[25]+f[0]) % mod

            for i in range(2,26):
                temp[i]=f[i-1]
            f=temp
        return sum(f) % mod
