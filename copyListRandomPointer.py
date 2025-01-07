class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        original = {}

        # Create dictionary that maps original nodes to new
        while curr:
            new = Node(curr.val)
            original[curr] = new
            curr = curr.next

        # Assign the pointers properly based on the mapping
        curr = head
        while curr:
            new = original[curr]
            new.next = original.get(curr.next) 
            new.random = original.get(curr.random) 
            curr = curr.next
        
        return original.get(head) 
