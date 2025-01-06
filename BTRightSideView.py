# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = []
        output = []
        queue.append(root)
        
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                print(queue)
            if level:
                output.append(level.pop())
        return output
