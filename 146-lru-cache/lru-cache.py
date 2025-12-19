class Node :
    def __init__ (self, key, value):
        self.key = key 
        self.value = value
        self.next = None
        self.prev = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left 

    def get(self, key: int) -> int:
        if key not in self.cache :
            return -1
        else :
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.cache : 
            node = self.cache[key]
            self.remove(node)
        node = Node(key,value)
        self.insert(node)
        self.cache[key] =node 
        if len(self.cache) > self.capacity :
            discard = self.left.next
            del self.cache[discard.key]
            self.remove(discard)

    def insert(self, node) :
        temp = self.right.prev
        self.right.prev = node 
        node.next = self.right 
        node.prev = temp
        temp.next = node 
    def remove (self,node) :
        previous = node.prev
        nex = node.next
        previous.next = nex 
        nex.prev = previous 
        

        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)