class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res=[]
        size=len(nums)
        for i in range(size):
            res.append(nums[nums[i]])
        return res