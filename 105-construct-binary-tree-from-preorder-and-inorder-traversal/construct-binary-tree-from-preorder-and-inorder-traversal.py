# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val : i for i, val in enumerate(inorder) }
        rootpointer =0 

        def dfs (l,r) :
            if l > r : 
                return None 
            nonlocal rootpointer 
            nodeval = preorder[rootpointer]
            rootpointer += 1 
            split = index[nodeval]
            node = TreeNode(nodeval)

            node.left = dfs(l,split -1) 
            node.right = dfs (split +1,r)
            return node
        return dfs (0,len(preorder)-1)
        