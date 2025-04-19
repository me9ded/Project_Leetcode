class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.binary_search(nums,upper+1)-self.binary_search(nums,lower)
    def binary_search(self,nums,number):
        l,r=0,len(nums)-1
        ret=0
        while l < r:
            temp=nums[l]+nums[r]
            if temp < number:
                ret+=r-l
                l+=1
            else:
                r-=1
        return ret


        