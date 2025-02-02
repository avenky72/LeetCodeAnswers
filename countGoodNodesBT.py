# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        count of good nodes
        in the stack have the recent visited node, and the largest value seen so far
        if the next node val is larger, increase the good nodes count
        update max val seen if needed
        """
        stack = [(root, root.val)]
        good = 0

        while stack:
            current, max_val_so_far = stack.pop()
            if max_val_so_far <= current.val:
                good += 1
            if current.left:
                stack.append((current.left, max(max_val_so_far, current.val)))
            if current.right:
                stack.append((current.right, max(max_val_so_far, current.val)))
        return good

                

        
