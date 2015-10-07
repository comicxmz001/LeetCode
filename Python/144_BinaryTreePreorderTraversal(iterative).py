# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #iteratively
        self.stack = [root]
        self.res = []
        while self.stack:
            self.node = self.stack.pop()
            if self.node:
                self.res.append(self.node.val)
                self.stack.append(self.node.right)
                self.stack.append(self.node.left)
        return self.res