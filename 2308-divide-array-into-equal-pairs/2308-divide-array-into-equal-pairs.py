class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for key,val in count.items():
            if val%2!=0:
                return False
        return True
        