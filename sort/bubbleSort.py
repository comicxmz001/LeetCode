def bubbleSort(alist):
	for passnum in range(0,len(alist)-1):
		for i in range (0,len(alist)-1o-passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i+1]
				alist[i+1] = alist[i]
				alist[i] = temp

a = [54,26,93,17,77,31,44,55,20]
bubbleSort(a)
print (a)
