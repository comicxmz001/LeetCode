# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = self.countNode(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count+1:
            return self.kthSmallest(root.right, k-count-1)
            
        return root.val
        
    def countNode(self, root):
        if not root:
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)