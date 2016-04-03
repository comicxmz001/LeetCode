# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 0
        dummy = head
        while dummy:
            prev = dummy
            dummy = dummy.next
            length += 1
        prev.next = head
        for _ in xrange(length - k%length):
            prev = head
            head = head.next
        prev.next = None
        return head