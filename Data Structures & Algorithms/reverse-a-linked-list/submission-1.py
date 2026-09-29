# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Doing this the iterative way: 

        prev, curr = None, head

        while curr:

            temp = curr.next # storing this variable 
            curr.next = prev # pointer is flipped, points to the prev node
            prev = curr # previous now is the current node
            curr = temp # current is now the next node

        return prev # return because curr is None, that is why the loop stoped