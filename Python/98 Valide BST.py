# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
        	return True
        if root.left:
        	l = root.left
        	while l:
        		if l.val > root.val:
        			return False
        		l = l.right
        if root.right:
        	r = root.right
        	while r:
        		if r.val < root.val:
        			return False
        		r = r.left
        return self.isValidBST(root.left) and self.isValidBST(root.right)
