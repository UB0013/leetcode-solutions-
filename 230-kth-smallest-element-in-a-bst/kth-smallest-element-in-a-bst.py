# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        result = None 
        inorder =[]
        def dfs (root):
            #nonlocal count
            #nonlocal result 
            if not root :
                return 
            left = dfs (root.left)
            inorder.append(root.val)
            #count = count +1 
            #if count == k :
                #result = root.val 
                #return 
            right = dfs (root.right)
            return 
        dfs(root)
        return inorder[k-1]
        

        



        