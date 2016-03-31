# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if empty or only has one node
        if not head or not head.next:
            return head
        
        # get the length of the linked list
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        # save the head to dummy
        dummy = ListNode(0)
        dummy.next = head
        
        # bottom up merge sort (1,2,4....)
        step = 1
        while step < length:
            print "step = " + str(step)
            cur = dummy.next # starting from the real head
            tail = dummy 
            # scan and merge the linked list by step
            while cur:
                left = cur # head of left part of list
                right = self.split(left,step) # head of right part
                cur = self.split(right,step) # update cur to the head of the 3rd segment
                tail = self.merge(left,right,tail) # merge left and right list, return the tail of newly merged list
                
            # up to next level merge operation
            step *= 2
        return dummy.next # this dummy.next is not the original head, as it has been updated by cur = dummy.next
        
    def split(self, head, n):
        prev = None
        for i in xrange(n):
            prev = head
            if not head:
                break
            head = head.next
        second = head
        if second: # if the head of second part is not None, then cut the tail of the first part
            prev.next = None # cut splited list
        return second
    
    def merge(self, l1, l2, head):
        # return the tail of merged list
        # head is a dummy head!
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        # now, at least one of the list is empty
        cur.next = l1 if l1 else l2
        
        # get to the tail (not none) of this newly merged list
        while cur.next:
            cur = cur.next
        return cur
        
        
        
        