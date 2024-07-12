# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return 

        dummy = ListNode()
        res = dummy
        minHeap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(minHeap, (lists[i].val,i,lists[i]))
        
        while minHeap:
            _,c, node = heappop(minHeap)
            res.next = node
            res = res.next 

            if node.next:
                heappush(minHeap, (node.next.val,c,node.next))
        
        return dummy.next


        

        

        
        