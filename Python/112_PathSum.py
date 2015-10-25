# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #if root is empty, return false
        if not root:
            return False
        # if not empty (root has a value), then deduct root.val from sum, 
        # if sum==0, then the path exists
        # else continue to check left child and right child. 
        # If any of the childs (OR) return True, then the tree has path, else not.
        sum -= root.val
        if sum == 0 and not root.left and not root.right: 
            #it is a leaf and the sum of path equals what we want
            return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right, sum)
        