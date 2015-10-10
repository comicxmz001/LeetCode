from ds import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tmp = ListNode(0)
        res = tmp
        tmp.next = head
        while tmp.next:
        	if tmp.next.val == val:
        		tmp.next = tmp.next.next
        	else:
        		tmp = tmp.next
        return res.next

#head = createLinkedList([])
head = createLinkedList([4,1,3,2,3,4])
val = 4
printList(Solution().removeElements(head,val))