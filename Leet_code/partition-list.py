# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        lessTail, greaterTail = less, greater
        curr = head

        while curr:
            if curr.val < x:
                lessTail.next = curr
                lessTail = lessTail.next
            else:
                greaterTail.next = curr
                greaterTail = greaterTail.next

            curr = curr.next
        
        lessTail.next = greater.next
        greaterTail.next = None

        return less.next
        
        

        