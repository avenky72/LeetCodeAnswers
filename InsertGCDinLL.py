# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a   

        curr = head

        while curr.next:
            c_next = curr.next
            temp = ListNode(gcd(curr.val, c_next.val), c_next)
            curr.next = temp
            temp.next = c_next
            curr = c_next
        
        return head
         
