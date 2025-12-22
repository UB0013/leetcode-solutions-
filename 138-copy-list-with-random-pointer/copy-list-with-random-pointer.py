"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head 

        copymap = {None:None}


        while curr :
            node =  Node(curr.val)
            copymap[curr]  = node 
            curr = curr.next 
        
        for value in copymap:
            if value : 
                copy = copymap[value] 
                copy.next = copymap[value.next]
                copy.random = copymap[value.random]

        return copymap[head]

        

        
        
        """{
            node : copynode  



        }"""

        