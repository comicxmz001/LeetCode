from ds import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		dummy_head = ListNode(0)
		dummy_head.next = head
		if not head:
			return head
		while head.next:
			if head.val == head.next.val:
				tmp = head.next #free unused pointer
				head.next = head.next.next
				tmp = None
			else:
				head = head.next
		return dummy_head.next

#head = createLinkedList([])
head = createLinkedList([1,1,1,2,2,3,4,4])
printList(Solution().deleteDuplicates(head))
a = None
