# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        count=1
        res=[]
        while temp.next.next:
            ans=temp.val
            ans1=temp.next.val
            ans2=temp.next.next.val
            if (ans > ans1 and ans1 < ans2) or (ans < ans1 and ans1> ans2):
                res.append(count)
            temp=temp.next
            count+=1
        if len(res)<2:
            return [-1,-1]
        max_distance=res[-1]-res[0]
        min_distance=min([res[i+1]-res[i] for i in range(len(res)-1)])
        return [min_distance,max_distance]


        