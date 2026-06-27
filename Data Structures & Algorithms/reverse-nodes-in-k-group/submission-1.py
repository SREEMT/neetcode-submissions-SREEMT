# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:
            # Check if there are k nodes
            check = curr
            for _ in range(k - 1):
                if not check:
                    break
                check = check.next

            if not check:
                tail.next = curr
                break

            # Detach the group
            next_group = check.next
            check.next = None

            # Reverse the group
            new_head = self.reverseGroup(curr)

            # Connect it
            tail.next = new_head
            tail = curr          # curr is now the tail after reversal
            curr.next = next_group

            # Move to the next group
            curr = next_group

        return dummy.next