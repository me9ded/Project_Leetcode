class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result=0
        for number in nums:
            current=str(number)
            size=len(current)
            if size%2==0:
                result+=1
        return result
        