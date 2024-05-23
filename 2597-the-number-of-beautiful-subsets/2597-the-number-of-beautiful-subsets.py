class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res=0
        def dfs(begin,seen):
            nonlocal res
            if begin>=len(nums):
                return
            for i in range(begin,len(nums)):
                if len(seen)!=0 and seen[nums[i]-k]!=0 or seen[nums[i]+k]!=0:
                    continue
                seen[nums[i]]+=1
                res+=1
                dfs(i+1,seen)
                seen[nums[i]]-=1
            return
        dfs(0,collections.defaultdict(int))
        return res
        