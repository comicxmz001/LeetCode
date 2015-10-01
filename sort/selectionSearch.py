def selectionSort(alist):
	for fillslot in range (len(alist)-1, 0, -1):
		positionofMax = 0;
		for location in range(1,fillslot+1):
			if alist[location] > alist[positionofMax]:
				positionofMax = location
		temp = alist[fillslot]
		alist[fillslot] = alist[positionofMax]
		alist[positionofMax] = temp


a = [54,26,93,17,77,31,44,55,20]
selectionSort(a)
print (a)
