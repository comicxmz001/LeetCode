def insertSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index
		#find the position that alist[position] > current, but alist[position-1]<current
		while position>0 and alist[position-1] > currentvalue:
			#always shifting right the values larger than current value
			alist[position] = alist[position-1]
			position = position-1
		alist[position] = currentvalue

a = [54,26,93,17,77,31,44,55,20]
insertSort(a)
print (a)