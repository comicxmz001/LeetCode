# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.path = []
        if not root:
            return []
        self.preOrder(root,'')
        return self.path
        
    def preOrder(self,root,curpath):
        curpath += str(root.val)+"->"
        if root.left:
            self.preOrder(root.left, curpath)
        if root.right:
            self.preOrder(root.right, curpath)
        if not root.left and not root.right:
            self.path.append(curpath[:-2])