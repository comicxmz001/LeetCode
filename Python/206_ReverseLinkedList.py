from ds import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return head
        prev = None
        cur = head
        nextnode = None
        while cur:
        	nextnode = cur.next
        	cur.next = prev
        	prev = cur
        	cur = nextnode
        return prev


n = []
head = createLinkedList(n)
printList(Solution().reverseList(head))