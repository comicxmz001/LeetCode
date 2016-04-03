#This algorithm do not require extra space.
#
def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist, first, last):
	if first < last:
		p = partition(alist,first,last)
		quickSortHelper(alist,first,p-1)
		quickSortHelper(alist,p+1,last)


def partition(alist, first, last):
	pivot = alist[last]
	divider = first
	for i in xrange(first,last):
		if alist[i] < pivot:
			alist[i],alist[divider] = alist[divider],alist[i]
			divider += 1

	# alist[divider], alist[pivot] = alist[pivot],alist[divider]
	alist[last] = alist[divider]
	alist[divider] = pivot

	return divider


	
	

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
