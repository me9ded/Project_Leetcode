class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=Counter(nums)
        res=max(d.values())
        return res*sum(i==res for i in d.values())