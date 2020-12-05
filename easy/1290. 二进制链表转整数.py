# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution:
    def getDecimalValue(self, head) -> int:
        res = 0
        length = 0
        tmp = head
        while tmp != None:
            length += 1
            tmp = tmp.next
        while head != None:
            if head.val == 1:
                res += math.pow(2,length-1)
            head = head.next
            length -= 1
        return int(res)