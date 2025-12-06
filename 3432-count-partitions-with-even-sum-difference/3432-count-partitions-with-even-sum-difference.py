class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result=0
        size=len(nums)
        result=0
        for i in range(size-1):
            left=sum(nums[0:i+1])
            right=sum(nums[i+1:size])
            temp=left-right
            if temp%2==0:
                result+=1
        return result
