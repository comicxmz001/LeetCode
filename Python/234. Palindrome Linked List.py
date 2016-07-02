#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head or not head.next:
			return True
		
		# find the mid and reverse the 2nd part of the list
		slow, fast = head, head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		# now, slow the median (first median in even len)
		slow.next = self.reverseList(slow.next)
		slow = slow.next
		while slow:
			if not slow.val == head.val:
				return False
			else:
				head = head.next
				slow = slow.next
		return True
	
	def reverseList(self,head):
		prev = None
		next = None
		while head:
			next = head.next
			head.next = prev
			prev = head
			head = next
		return prev