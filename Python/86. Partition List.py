#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		
		# dummyhead
		dummyhead = ListNode(0)
		tails = dummyhead
		
		prev = ListNode(0)
		prev.next = head
		curr = prev
		# process the list
		while curr.next:
			if curr.next.val < x:
				curr = curr.next
			else:
				# head.val > x, move to the tail
				tails.next = ListNode(curr.next.val)
				tails = tails.next
				curr.next = curr.next.next
		curr.next = dummyhead.next
		return prev.next