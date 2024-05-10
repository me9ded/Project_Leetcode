class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minheap=[]
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                heappush(minheap,(arr[i]/arr[j],(arr[i],arr[j])))
        for _ in range(k):
            a,b=heappop(minheap)[1]
        return [a,b]

