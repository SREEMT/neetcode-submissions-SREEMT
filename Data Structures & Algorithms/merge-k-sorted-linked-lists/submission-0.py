# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = node = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        merged = self.mergeTwoLists(lists[0], lists[1])
        i = 2
        while i < len(lists):
            merged = self.mergeTwoLists(merged, lists[i])
            i += 1
        return merged
            


        