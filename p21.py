# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        cur = result
        while l1 or l2:
            if cur is None:
                result = ListNode(0)
                cur = result
            else:
                cur.next = ListNode(0)
                cur = cur.next
            if l1 is None:
                cur.val = l2.val
                l2 = l2.next
            elif l2 is None:
                cur.val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                cur.val = l1.val
                l1 = l1.next
            else:
                cur.val = l2.val
                l2 = l2.next
        return result
        