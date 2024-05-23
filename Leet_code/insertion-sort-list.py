# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        back = head
        front = head.next
        
        while front:
            if back.val <= front.val:
                back = front
                front = front.next
            else:
                temp = dummy

                while temp.next.val < front.val:
                    temp = temp.next
                
                back.next = front.next
                front.next = temp.next
                temp.next = front
                front = back.next
            
        return dummy.next

                


            



        