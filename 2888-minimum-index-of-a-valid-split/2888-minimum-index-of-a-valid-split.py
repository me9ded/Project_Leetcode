class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        x,f=max(count.items(),key=lambda x:x[1])
        size=len(nums)
        second_map=Counter()
        second_map_size=0

        for i in range(size):
            second_map[nums[i]]+=1
            second_map_size+=1

            right_count=f-second_map.get(x,0)
            right_size=size-second_map_size

            if(second_map.get(x,0) * 2 > second_map_size and right_count * 2 > right_size):
                return i
        return -1
            
            
        