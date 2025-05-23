class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        max_sum=sum(max(n,k^n) for n in nums)
        count=sum((n^k) > n for n in nums)
        return max_sum-(min(abs(n-(n^k)) for n in nums) if count%2 else 0)
        
        