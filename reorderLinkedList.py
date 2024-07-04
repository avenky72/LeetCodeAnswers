# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        first = head
        last = head.next
        mid = head
        #end = head.next
        count = 1

        #while last.next != None:
        while last:
            last = last.next
            count += 1

        half = (count)//2
        
        for i in range(half):
            mid = mid.next
        
        #for i in range(half-2):
        #    end = end.next
        #end.next = None

        prev = None
        curr = mid
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        

        first = head
        second = prev
        while second.next:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
