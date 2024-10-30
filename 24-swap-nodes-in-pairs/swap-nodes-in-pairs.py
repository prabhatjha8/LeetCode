# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head 
        else:
            first_item = head
            second_item = head.next
            third_item = self.swapPairs(second_item.next)
            second_item.next = first_item
            first_item.next = third_item
            return second_item
        