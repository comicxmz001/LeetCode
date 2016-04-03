# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def floor(key):
	# find the largest val that <= key
	x = floorHelper(root,key)
	if not x:
		return None
	return x

def floorHelper(node, key):
	if not node:
		return None

	if node.val == key:
		return node

	if node.val > key:
		return floorHelper(node.left)

	# node.val < key
	# continue to find if there is any element k,
	# that node.val < k < key, which means search right child
	
	t = floorHelper(node.right)
	if not t:
		return t
	return node.val

	
	