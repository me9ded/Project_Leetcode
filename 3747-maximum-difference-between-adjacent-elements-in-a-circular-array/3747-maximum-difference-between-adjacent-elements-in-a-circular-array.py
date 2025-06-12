class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        size=len(nums)
        result=abs(nums[size-1]-nums[0])
        for i in range(size-1):
            result=max(result,abs(nums[i]-nums[i+1]))
        return result