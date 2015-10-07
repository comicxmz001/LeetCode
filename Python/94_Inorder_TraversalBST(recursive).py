# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        return self.it(root)
    def it(self, root):
        if root == None:
            return []
        self.it(root.left)
        self.res.append(root.val)
        self.it(root.right)
        return self.res