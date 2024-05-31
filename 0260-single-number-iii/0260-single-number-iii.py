class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=[]
        num_count=Counter(nums)
        for number,val in num_count.items():
            if val==1:
                res.append(number)
        return res
        