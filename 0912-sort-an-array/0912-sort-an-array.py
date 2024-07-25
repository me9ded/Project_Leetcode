class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        min_val,max_val=min(nums),max(nums)
        counts=[0]*(max_val-min_val+1)
        for num in nums:
            counts[num-min_val]+=1
        j=0
        for i in range(len(counts)):
            while counts[i]>0:
                nums[j]=i+min_val
                j+=1
                counts[i]-=1
        return nums
        