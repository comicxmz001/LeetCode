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
        self.res = []
        self.pt(root,self.res)
        return self.res
        
    def pt(self, root, res):
        if root == None:
            return []
        self.res.append(root.val)
        self.pt(root.left,res)
        self.pt(root.right,res)
        return self.res