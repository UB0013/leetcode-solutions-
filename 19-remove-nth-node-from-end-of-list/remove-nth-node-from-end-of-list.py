# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove = head 
        curr = ListNode(0,head)
        tail = curr
      

        while n >0 :
            remove = remove.next
            n = n-1
        while remove: 
            curr = curr.next
            remove = remove.next 
        curr.next = curr.next.next
        return tail.next

        


        