class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(n,sys.maxsize):
            bin_i = bin(i)
            bin_i = bin_i[2:]
            if "0" not in bin_i:
                return i