# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_d = [0]
        def diameter(root):
            if not root:
                return 0
            
            l_child_dia = diameter(root.left)
            r_child_dia = diameter(root.right)
            curr_dia = l_child_dia + r_child_dia
            max_d[0] = max(max_d[0], curr_dia)

            return (1 + max(l_child_dia, r_child_dia))
        
        diameter(root)
        return max_d[0]
