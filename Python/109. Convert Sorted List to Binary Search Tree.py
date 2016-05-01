# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self._sortedListToBST(head, None)
    
    def _sortedListToBST(self, start, end):
        if not start or start == end:
            return None
        slow = start
        fast = start
        
        while not fast.next == end and not fast.next.next == end:
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.val)
        root.left = self._sortedListToBST(start, slow)
        root.right = self._sortedListToBST(slow.next, end)
        return root    