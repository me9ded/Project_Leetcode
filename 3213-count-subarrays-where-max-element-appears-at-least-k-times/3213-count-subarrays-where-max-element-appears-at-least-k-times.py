class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start=0
        ans=0
        cnt=0
        res=max(nums)
        for end in range(len(nums)):
            if nums[end]==res:
                cnt+=1
            while cnt==k:
                if nums[start]==res:
                    cnt-=1
                start+=1
            ans+=start
        return ans