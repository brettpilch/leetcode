# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        output = head
        while head:
            nextnode = head.next
            if nextnode is None:
                return output
            if nextnode.val == head.val:
                head.next = nextnode.next
            else:
                head = head.next
        return output
        