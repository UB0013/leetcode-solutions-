# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 

        while curr :
            temp = curr.next # 2
            curr.next = prev #N
            prev = curr
            curr = temp 
            # 1-N
        return prev


# curr = 1
# temp 2 
# 1- N
# prev = 2
# curr = 2 











