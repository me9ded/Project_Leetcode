class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sum_1=nums[0]+nums[1]
        sum_2=nums[0]+nums[2]
        sum_3=nums[1]+nums[2]

        if sum_1 > nums[2] and sum_2 > nums[1] and sum_3 > nums[0]:
            count=Counter(nums)
            if len(list(count.items()))==1:
                return "equilateral"
            elif len(list(count.items()))==2:
                return "isosceles"
            elif len(list(count.items()))==3:
                return "scalene"
        return 'none'