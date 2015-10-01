def insertSort(alist):
	for index in range(1,len(alist)):
		currentvalue=alist[index]
		position = index
		while position>0 and alist[position-1]> currentvalue:
			alist[position] = alist [position-1]
			position = position-1
		alist[position] = currentvalue

def bubbleSort(alist):
	for passnum in range(0,len(alist)-1):
		for i in range (0,len(alist)-1o-passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i+1]
				alist[i+1] = alist[i]
				alist[i] = temp

def selectionSort(alist):
	for fillslot in range (len(alist)-1, 0, -1):
		positionofMax = 0;
		for location in range(1,fillslot+1):
			if alist[location] > alist[positionofMax]:
				positionofMax = location
		temp = alist[fillslot]
		alist[fillslot] = alist[positionofMax]
		alist[positionofMax] = temp

#Shell sort, a variation of selection sort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue		

#Merge sort algorithm
def mergeSort(alist):
    print ("Splitting ", alist)
    if len(alist)>1:
        midindex = len(alist)//2
        lefthalf = alist[:midindex]
        righthalf = alist[midindex:]

        #recurs till each half contains only 1 or 0 elements
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #Now start merging
        
        leftposition = 0 #left half index
        rightposition = 0 #right half index
        # the position of received original list, staring from 0
        # fill in sorted elements
        position = 0    

        #If both halves have elements
        while leftposition < len (lefthalf) and rightposition < len(righthalf):
            if lefthalf[leftposition] < righthalf[rightposition]:
                alist[position] = lefthalf[leftposition]
                leftposition = leftposition + 1
            else:
                alist[position] = righthalf [rightposition]
                rightposition = rightposition + 1
            position = position + 1

        #If only left half has elements
        while leftposition < len(lefthalf):
            alist[position] = lefthalf[leftposition]
            leftposition = leftposition + 1
            position = position + 1
        
        #If only right half has elements
        while rightposition < len(righthalf):
            alist[position] = righthalf[rightposition]
            rightposition = rightposition + 1
            position = position + 1
            
    print ("Merging ", alist)				

a = [54,26,93,17,77,31,44,55,20]
insertSort(a)
print (a)