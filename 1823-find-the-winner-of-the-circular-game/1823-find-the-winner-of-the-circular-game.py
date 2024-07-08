class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        temp=list(range(1,n+1))
        start=0
        while len(temp)>1:
            value_to_remove=(start+k-1)%len(temp)
            temp.pop(value_to_remove)
            start=value_to_remove
        return temp[0]

        