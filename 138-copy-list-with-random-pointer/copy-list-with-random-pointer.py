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
        copymap = {None:None}
        curr = head
        while curr : 
            copymap[curr] = Node(curr.val)
            curr = curr.next 
        print (copymap.items())
        
        for key,value  in copymap.items():
            if key and value : 
                value.random = copymap[key.random]
                value.next = copymap[key.next]
        return copymap[head]



