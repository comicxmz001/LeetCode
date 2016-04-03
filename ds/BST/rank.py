# rank will use size(node x) function, 
# which returns the number of subnodes under node x

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.cout = None

def size(node):
	if not node:
		return 0
	return node.cout

def rank(key, root):
	if not root:
		return 0
	if key < root.val:
		return rank(root.left)
	elif key > root.val:
		return rank(root.left) + 1 + rank(root.right)
	else:
		return size(root.left)
	