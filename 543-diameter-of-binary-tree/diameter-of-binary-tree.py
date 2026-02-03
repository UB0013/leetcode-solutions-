# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0 
        res = 0 
        def dfs (root) :
            nonlocal res 
            nonlocal dia 
            if not root :
                return 0 
            left = dfs (root.left)
            right = dfs(root.right)
            # nonlocal dia 
            dia = left + right
            res = max(res,dia)
            return 1 + max(left,right)

        dfs (root)

        return res  

        
        