class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        size=len(nums)
        temp=[0]*(size+1)
        k=0
        total_sum=0
        for i in range(size):

            while total_sum+temp[i] < nums[i]:
                k+=1

                if k > len(queries):
                    return -1
                left,right,val=queries[k-1]
                if right >=i:
                    temp[max(left,i)]+=val
                    temp[right+1]-=val
            total_sum+=temp[i]
        return k