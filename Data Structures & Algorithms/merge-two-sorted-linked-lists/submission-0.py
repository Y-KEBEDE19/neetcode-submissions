# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        tail = dummy
        # Approach: 

        # first while loop, goes until we reach the end of the shorter list

        # second loop just addds the rest of the remaining list if it exists
        
        # 

        while list1 and list2: # whlie these two lists are not none
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: # this handles list2.val < list1.val && list1.val == list2.val
                tail.next = list2
                list2= list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

