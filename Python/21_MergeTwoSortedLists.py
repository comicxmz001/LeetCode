from ds import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #new list
        res = ListNode(0)
        head = res
        if not l1:
        	return l2
        elif not l2:
        	return l1
        else:
        	while l1 and l2:
        		if l1.val < l2.val:
        			res.next = l1
        			res = res.next
        			l1 = l1.next
        		else:
        			res.next = l2
        			res = res.next
        			l2 = l2.next
			if l1 and not l2:
				res.next = l1
			elif not l1 and l2:
				res.next = l2
		return head.next


l1 = createLinkedList([])
l2 = createLinkedList([])

printList(Solution().mergeTwoLists(l1,l2))