class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res=0
        maxind=-1
        minind=-1
        nonelement=-1
        for ind,num in enumerate(nums):
            if num==minK:
                minind=ind
            if num==maxK:
                maxind=ind
            if not minK<=num<=maxK:
                nonelement=ind
            res+=max(0,min(minind,maxind)-nonelement)
        return res 