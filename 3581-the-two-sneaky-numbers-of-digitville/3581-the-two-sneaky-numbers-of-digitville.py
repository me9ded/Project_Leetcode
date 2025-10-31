class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []
        for number,freq in count.items():
            if freq == 2 :
                result.append(number)
        return result