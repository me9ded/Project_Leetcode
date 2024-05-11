class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(quality)
        cost=float("inf")
        total=0
        wage_to_quality=[]
        for i in range(n):
            wage_to_quality.append((wage[i]/quality[i],quality[i]))
        wage_to_quality.sort(key=lambda x:x[0])
        res=[]
        for i in range(n):
            heapq.heappush(res,-wage_to_quality[i][1])
            total+=wage_to_quality[i][1]
            if len(res)>k:
                total+=heapq.heappop(res)
            if len(res)==k:
                cost=min(cost,total*wage_to_quality[i][0])
        return cost
            
