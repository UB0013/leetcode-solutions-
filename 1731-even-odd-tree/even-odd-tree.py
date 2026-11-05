# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        q = deque ()
        q.append(root)
        level = 0 

        while q :
            lenq = len (q)
            prev = float ("-inf") if level%2 == 0 else float("inf")
            for i in range (lenq) : 
                node = q.popleft()
                print(node.val)
                if level%2 == 0 : 
                    if node.val%2 == 0 or prev >= node.val :
                            return False 
                else : 
                    if node.val%2 != 0 or prev <= node.val :
                            return False 
                if node.left :
                    q.append(node.left)
                if node.right : 
                    q.append(node.right) 
                prev = node.val  
            level +=1 
        
        return True




        