# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
	Time exceed with Python!!!!
	Pass with C/C++
"""
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return head
        Helper = ListNode(0) #Head of sorted list
        Previous = Helper	#Insert node between previous and previous.next
        Current = head	#The node to be inserted
        Next = None	#The next node to be inserted
        tail = Helper

        while Current:
        	Next = Current.next
            if Current.val > tail.val:
                tail.next = Current
                Current = Next
                Previous = Helper
            else:
            	#find the right place to insert
            	#Always use Previous.next, because Previous is just a head used to create a new list
            	while Previous.next and Previous.next.val < Current.val:
            		Previous = Previous.next
            	#Find the right place, start inserting
            	Current.next = Previous.next
            	Previous.next = Current #Insert current
                tail = Previous.next
                Previous = Helper #move back to the head, prepare next insert
                Current = Next #Move to the next node which is going to be inserted next.
        #once completed. Return helper.next 
        return helper.next
        