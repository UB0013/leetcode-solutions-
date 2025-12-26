# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        res =[]
     
        def dfs (root) : 
            nonlocal res 
            if not root :
                res.append("N")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(",".join(res))
        return ",".join(res) 



        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        """

        i = 0 

        def dfs ():
            nonlocal i  
            values = data.split(",")
          
            if values[i] == "N" :
                i = i +1 
                return None
                
            node = TreeNode(values[i])
            i = i+1 
            node.left = dfs ()
            node.right = dfs()
            return node 
        return dfs ()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans