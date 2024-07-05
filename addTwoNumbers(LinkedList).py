# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = ListNode(0)
        curr = l3
        carry = 0

        while l1 or l2 or carry:
            x = carry
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next
            
            curr.next = ListNode(x%10)
            curr = curr.next
            carry = x // 10

        return l3.next
