# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        curr = head
        seen = set()  
        
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
                curr = curr.next
        
        return False
                    
