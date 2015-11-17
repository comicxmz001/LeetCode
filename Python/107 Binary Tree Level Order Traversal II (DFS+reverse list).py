# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.levelOrderTraversal(root,0)
        return self.res[::-1]
        
    def levelOrderTraversal(self,root,level):
        if root == None:
            return None
        if len(self.res) == level:
            self.res.append([])
        self.res[level].append(root.val)
        self.levelOrderTraversal(root.left,level+1)
        self.levelOrderTraversal(root.right,level+1)

# 60ms runtime