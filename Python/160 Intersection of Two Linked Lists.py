# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        if not p1 or not p2:
            return None
        while p1 and p2 and (p1 is not p2):
            p1 = p1.next
            p2 = p2.next
            
            if p1 is p2:
                return p1
            
            if not p1:
                p1 = headB
            if not p2:
                p2 = headA
        return p1

"""
If there is an intersection
A1 -> A2 -> C1
B1 -> C1

THEN:
A1 -> A2 -> C1  -> None -> B1 ->C1
B1 -> C1 -> None-> A1   -> A2 ->C1

if thre is no intersection
A1 -> A2 -> C1
B1

THEN:
A1 -> A2 -> C1 -> B1 -> None
B1 -> A1 -> A2 -> C1 -> None

Here, p1 == p2 == None, break. then return None. 

"""