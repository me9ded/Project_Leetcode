class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time=0
        ans=0
        for order in customers:
            time=max(order[0],time)+order[1]
            ans+=time-order[0]
        return ans/len(customers)
