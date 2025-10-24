class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1,sys.maxsize):
            i_string=str(i)
            count = Counter(i_string)
            if all(count[j] == int(j) for j in count):
                return i
