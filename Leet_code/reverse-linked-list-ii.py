# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left:
            return head
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        for _ in range(left):
            prev = curr
            curr = curr.next
            
        left1 = curr
        prev1 = None

        for _ in range(right-left+1):
            curr.next, prev1, curr = prev1, curr, curr.next
        
        prev.next = prev1
        left1.next = curr

        return dummy.next


        
        



        

        
        

        


        




        
        


        