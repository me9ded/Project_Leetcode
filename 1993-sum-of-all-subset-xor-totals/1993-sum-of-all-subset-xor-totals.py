class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        size=len(nums)
        def dfs(index,number):
            if index==size:
                return number
            included=dfs(index+1,number^nums[index])
            excluded=dfs(index+1,number)
            return included+excluded
        return dfs(0,0)
        