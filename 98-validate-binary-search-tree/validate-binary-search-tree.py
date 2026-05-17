# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs (lb, rb, root): 
            if not root : 
                return True 
            if lb< root.val< rb :
                return dfs (lb, root.val, root.left) and  dfs (root.val,rb, root.right) 
            else :
                return False 
        return dfs (float("-inf"), float ("inf"),root)
