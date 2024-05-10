# Rreturn the depth of a binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        children = [root]
        count = 0
        
        while len(children) > 0:
            count += 1
            nodes = len(children)
            for i in range(nodes):
                curr = children.pop(0)
                if curr.left:
                    children.append(curr.left)
                if curr.right:
                    children.append(curr.right)
                #print(children, "count: ", count)
        return count
