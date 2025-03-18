class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result=1
        for i in range(len(nums)-result):
            current=1
            used=nums[i]
            for end in range(i+1,len(nums)):
                if(used & nums[end])==0:
                    used |=nums[end]
                    current+=1
                else:
                    break
            result=max(result,current)
        return result
        