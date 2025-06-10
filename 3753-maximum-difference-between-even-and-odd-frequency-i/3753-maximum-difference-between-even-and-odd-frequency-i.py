class Solution:
    def maxDifference(self, s: str) -> int:
        result=0
        count_freq=Counter(list(s))
        max_odd=-1
        min_even=float("inf")
        for val in count_freq.values():
            if val%2!=0:
                max_odd=max(max_odd,val)
            else:
                min_even=min(min_even,val)
        result=max_odd-min_even
        return result