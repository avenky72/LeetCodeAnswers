# Invert a Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        children = [root]
        if root is None:
            return None

        while len(children) > 0:
            curr = children.pop(0)
            #both
            if curr.left and curr.right:
                curr.left, curr.right = curr.right, curr.left
            # only left or right
            elif curr.left:  
                curr.right = curr.left
                curr.left = None
            elif curr.right: 
                curr.left = curr.right
                curr.right = None
            if curr.left:
                children.append(curr.left)
            if curr.right:
                children.append(curr.right)
        return root
