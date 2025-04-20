class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        result=0
        for val in count:
            result+=ceil(float(count[val])/(val+1))*(val+1)
        return int(result)