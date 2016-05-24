def towerOfHanoi(n, source, dest, helper):
	# need to move n-1 disks to the helper peg (peg C), 
	# then move the largest disk (nth disk) to its final destination (peg B), the nth disk will not be moved anymore.
	# then move the n-1 disks from helper peg (peg C) to the destination peg (peg B)
	# the process repeats as a natural recursion

	 if n > 0:
		towerOfHanoi(n-1,source, helper, dest)
		print("Moving disk from {} to {}".format(source,dest))
		towerOfHanoi(n-1,helper, dest, source)       

towerOfHanoi(3,'A','B','C')