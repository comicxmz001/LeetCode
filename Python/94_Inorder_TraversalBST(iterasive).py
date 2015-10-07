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
        self.stack = []
        self.res = []
        self.curNode = root
        while self.curNode or len(self.stack)>0:
            while self.curNode:
                self.stack.append(self.curNode)
                self.curNode = self.curNode.left
            self.curNode = self.stack.pop()
            self.res.append(self.curNode.val)
            self.curNode = self.curNode.right
        return self.res