class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result=0
        size=len(nums)
        count_zero=0
        start=0
        for i in range(size):
            count_zero+=(nums[i]==0)
            while count_zero > 1:
                count_zero-=(nums[start]==0)
                start+=1
            result=max(result,i-start)
        return result


