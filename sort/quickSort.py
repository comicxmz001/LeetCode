#This algorithm requires additional memory
#
def quickSort(alist):
	
	less = []
	equal = []
	greater = []

	if len(alist) > 1:
		pivot = alist[0] #Pick the first element as pivot
		for x in alist:
			if x < pivot:
				less.append(x)
			elif x == pivot:
				equal.append(x)	
			else:
				greater.append(x)
		return quickSort(less) + equal + quickSort(greater)
	else:
		return alist

alist = [54,26,93,17,77,31,44,55,20]
alist = quickSort(alist)
print(alist)
