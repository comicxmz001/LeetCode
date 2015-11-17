# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from ds import *
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if len(nums) == 0: 132 ms
        if not nums: # 96ms
        	return None
        pivot = len(nums)/2
        root = TreeNode(nums[pivot])
        root.left = self.sortedArrayToBST(nums[:pivot])
        root.right = self.sortedArrayToBST(nums[pivot+1:])

        return root

if __name__ == '__main__':
	arr = [1,2,3,4]
	Solution().sortedArrayToBST([])