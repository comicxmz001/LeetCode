import ds

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if (m==n):
        	return head
        dummy = ds.ListNode(0)
        dummy.next = head
        prev = dummy
        for i in xrange(m-1):
        	prev = prev.next
        # reverse then [m,n] nodes
        start = prev.next
        then = start.next
        for i in xrange(n-m):
        	start.next = then.next
        	then.next = prev.next
        	prev.next = then
        	then = start.next
        return dummy.next

if __name__ == '__main__':
	l = ds.createLinkedList([1,2,3,4,5])
	ds.printList(Solution().reverseBetween(l,2,2))