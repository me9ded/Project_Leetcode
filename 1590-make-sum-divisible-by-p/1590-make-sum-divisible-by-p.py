class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res=0
        n=len(nums)
        total_sum=0
        for num in nums:
            total_sum=(total_sum+num)%p
        target=total_sum%p
        if target==0:
            return 0
        hash_map={0:-1}
        current=0
        min_len=n
        for i in range(n):
            current=(current+nums[i])%p
            needed=(current-target+p)%p
            if needed in hash_map:
                min_len=min(min_len,i-hash_map[needed])
            hash_map[current]=i
        return -1 if min_len==n else min_len