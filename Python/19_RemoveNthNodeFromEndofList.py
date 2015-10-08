# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0 #list length
        helper = head
        while head:
            count += 1
            head = head.next
        count -= n #calculate iterate times
        if count == 0: # Remove the head node.
            return helper.next
        #Set head back to its original address.
        head = helper
        #Locate the previous node of the target node.
        for i in xrange(count-1):
            head = head.next
        #remove node
        head.next = head.next.next
        return helper
                
        
        
        
        