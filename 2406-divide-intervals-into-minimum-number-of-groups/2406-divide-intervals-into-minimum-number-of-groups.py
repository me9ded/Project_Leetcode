class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_point=sorted(interval[0] for interval in intervals)
        end_point=sorted(interval[1] for interval in intervals)
        group_count=0
        end_time=0
        for start in start_point:
            if start > end_point[end_time]:
                end_time+=1
            else:
                group_count+=1
        return group_count  

        