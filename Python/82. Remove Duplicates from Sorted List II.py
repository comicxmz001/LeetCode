#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		
		recursively delete duplicated nodes
		"""
		if not head: return None
		
		# if the given head and head.next are duplicated nodes
		if head.next and head.val == head.next.val:
			# skip all the duplicated elements and calculate
			while head.next and head.val == head.next.val:
				head = head.next 
			# after the while loop, head is a non-duplicated element
			# e.g. [2,2,3,4]: head is now set to 3 (2,2 are skipped)
			head = self.deleteDuplicates(head.next)
		else:
			# we know head.val != head.next.val
			# however, we don't know the relationship between head.next.val and head.next.next.....val
			# so, we continue to calculate the rest of list that starts with head.next
			head.next = self.deleteDuplicates(head.next)
		return head