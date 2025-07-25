class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set_nums=set([num for num in nums if num > 0])
        return max(nums) if len(set_nums)==0 else sum(set_nums)