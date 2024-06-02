# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        """ after is curr.next (regular) and prev is curr.previous, so to make reverse,
        prev needs to be curr.next, while after is a temp variable to update curr"""
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev
            
