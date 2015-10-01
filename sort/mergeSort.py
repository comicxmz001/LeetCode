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

alist = [54,26,93,17,77,31,44,55,20]

mergeSort(alist)
print(alist)

