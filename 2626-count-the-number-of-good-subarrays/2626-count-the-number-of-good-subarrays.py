class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        size=len(nums)
        common,right=0,-1
        freq=Counter()
        result=0
        for left in range(size):
            while common < k and right+1 < size:
                right+=1
                common+=freq[nums[right]]
                freq[nums[right]]+=1
            if common >= k:
                result+=size-right
            freq[nums[left]]-=1
            common-=freq[nums[left]]
        return result
