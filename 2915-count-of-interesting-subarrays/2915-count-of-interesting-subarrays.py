class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res=0
        prefix=0
        cnt=Counter([0])
        n=len(nums)
        for i in range(n):
            prefix+=1 if nums[i] % modulo==k else 0
            res+=cnt[(prefix-k+modulo)%modulo]
            cnt[prefix%modulo]+=1
        return res