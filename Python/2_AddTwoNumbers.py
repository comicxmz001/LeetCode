# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l2:
            return l1
        if not l1:
            return l2
        headl2 = l2
        while l1 and l2:
            l2.val = l1.val + l2.val
            if l2.val > 9:
                l2.val %= 10
                if l2.next:
                    l2.next.val +=1
                else:
                    l2.next = ListNode(1)
            l1 = l1.next
            l2parent = l2
            l2 = l2.next
        if l1 and not l2:#l2 empty
            l2parent.next = ListNode(l1.val)
            l2parent.next.next = l1.next
        elif not l1 and l2: #l1 empty
            while l2:
                if l2.val >9:
                    l2.val %= 10
                    if not l2.next:
                        l2.next = ListNode(1)
                    else:
                        l2.next.val += 1
                l2 = l2.next
        else: #both empty
            return headl2
        return headl2
            