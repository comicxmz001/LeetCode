# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Stop conditions
        if not root:
        	return None

        #Different sides, return root
        if min(p.val,q.val) <= root.val <= max(p.val,q.val):
        	return root
        if max(p.val,q.val) < root.val: # Go left
        	return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val,q.val) > root.val: # Go right
        	return self.lowestCommonAncestor(root.right,p,q)
