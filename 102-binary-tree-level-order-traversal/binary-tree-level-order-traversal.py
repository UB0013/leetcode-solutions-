# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append(root)
        #q. = [9,20]
        # output = [[3]]

        output = []
        level =  [] 
        if not root :
            return []
        while q : 
            lenq = len(q) # 2
            level = [] # [] 
            for i in  range (lenq) : # 0 1 

                node = q.popleft() # 20 
                if node : 
                    level.append(node.val) # [9,20]
                    if node.left : #
                        q.append(node.left) 
                    if node.right : 
                        q.append(node.right) # q [15,7]

            output.append(level) # [ [3] [9,20],  
        return output 
            





        