class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N=len(nums)
        freq=[0]*(N+1)
        for num in nums:
            freq[min(N,num)]+=1
        number_greater_or_equal=0
        for i in range(N,0,-1):
            number_greater_or_equal+=freq[i]
            if i==number_greater_or_equal:
                return i
        return -1

            

