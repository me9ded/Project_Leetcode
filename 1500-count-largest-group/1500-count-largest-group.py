class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq=collections.Counter()
        for i in range(1,n+1):
            key=sum(int(j) for j in str(i))
            freq[key]+=1
        maxval=max(freq.values())
        result=sum(1 for val in freq.values() if val==maxval)
        return result 