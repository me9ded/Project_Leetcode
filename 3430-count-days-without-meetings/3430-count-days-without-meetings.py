class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        result=0
        count=0
        meetings.sort()
        for start,end in meetings:
            if start > count+1:
                result+=start-count-1
            count=max(count,end)
        result+=days-count
        return result
            
        