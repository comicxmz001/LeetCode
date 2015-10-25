"""
	This file includes several data structures used in LeetCode question.
"""
# Definition for a list node.
class ListNode(object):
	def __init__(self, n):
		self.val = n
		self.next = None

def createLinkedList(nodelist):
	#type nodelist: list[int/float]
	#rtype: head of linked list
	linkedList = ListNode(0)
	head = linkedList
	for val in nodelist:
		linkedList.next = ListNode(val)
		linkedList = linkedList.next
	return head.next

def printList(head):
	if not head:
		print "head is None!\n"
		return
	else:
		while head:
			print head.val
			head = head.next
		return 

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

#TODO finish createBinaryTree
def createBinaryTree(nodelist):
	root = TreeNode(0)
	l = len(nodelist) 
	if l == 0:
		return None

if __name__ == '__main__':
# main()
	n = [1,2,3]
	bst = createBinaryTree(n)