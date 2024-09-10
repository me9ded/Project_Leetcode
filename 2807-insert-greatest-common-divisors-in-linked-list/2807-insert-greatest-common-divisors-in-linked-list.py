# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head.next
        prev=head
        while cur:
            pgcd=math.gcd(prev.val,cur.val)
            element=ListNode(pgcd)
            prev.next=element
            element.next=cur
            prev=cur
            cur=cur.next
        return head

