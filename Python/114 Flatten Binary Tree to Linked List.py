# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# using global variables may cause unexpected result, 
# instead declare another function and use original function to 
# declare a local member to avoid potential disaster.

class Solution(object):
    def flatten(self, root):
        self.prev = None
        self.doflatten(root)
        
    def doflatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.doflatten(root.right)
        self.doflatten(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root