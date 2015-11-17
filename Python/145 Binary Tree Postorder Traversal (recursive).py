# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.postorder(root)
        return self.res
        
    def postorder(self,node):
        if node == None:
            return None
        self.postorder(node.left)
        self.postorder(node.right)
        self.res.append(node.val)