# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddTurn = True
        odd = ListNode()
        even = ListNode()
        oddTail= odd
        evenTail = even

        while head:
            if oddTurn:
                oddTail.next = head
                oddTail = oddTail.next
                oddTurn = False
            else:
                evenTail.next = head
                evenTail = evenTail.next
                oddTurn = True
            
            head = head.next
        
        oddTail.next = even.next
        evenTail.next = None

        return odd.next

        