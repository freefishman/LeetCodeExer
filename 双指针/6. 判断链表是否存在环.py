# 141. Linked List Cycle (Easy)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while True:
            if fast == slow:
                return True
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
Solution.hasCycle(ListNode([3,2,0,-4]))