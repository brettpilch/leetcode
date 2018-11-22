# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        thisnode = result
        while l1 or l2:
            this = thisnode.val
            if l1:
                this += l1.val
                l1 = l1.next
            if l2:
                this += l2.val
                l2 = l2.next
            thisnode.val = this % 10
            carry = this // 10
            if (l1 or l2) or carry:
                thisnode.next = ListNode(carry)
                thisnode = thisnode.next
        return result
            
        