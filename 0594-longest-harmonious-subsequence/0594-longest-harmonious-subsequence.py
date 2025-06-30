class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        size=len(nums)
        j=0
        for i in range(size):
            while nums[i]-nums[j] > 1:
                j+=1
            if nums[i]-nums[j]==1:
                result=max(result,i-j+1)
        return result