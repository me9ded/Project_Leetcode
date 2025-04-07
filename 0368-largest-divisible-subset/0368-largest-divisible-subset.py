class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        size=len(nums)
        result=[[nums[i]] for i in range(size)]

        for i in range(1,size):
            current=[]
            for j in range(i):
                last=result[j][-1]
                if last%result[i][0]==0 or result[i][0]%last==0:
                    current.append(result[j]+result[i])
            current.sort(key=len)
            if current:
                result[i]=current[-1]
        result.sort(key=len)
        return result[-1]

        