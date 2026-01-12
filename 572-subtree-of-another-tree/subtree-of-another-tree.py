# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
     
        def dfs (root, subRoot) : 
            if not subRoot :
                return True 
            if not root :
                return False
            if sametree(root,subRoot) == True :
                return True 
            else:
                return dfs (root.left,subRoot) or dfs (root.right,subRoot)
        def sametree (root,subroot):
            if not root and not subroot:
                return True 
            if root and subroot and root.val == subroot.val:
                return sametree (root.left ,subroot.left) and sametree (root.right,subroot.right)
            if not root or not subroot or root.val != subroot.val :
                return False 
            

        return dfs (root,subRoot)
        

            
        