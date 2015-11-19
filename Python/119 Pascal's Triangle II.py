class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex<= 0:
        	return [1]
        T = [0 for x in xrange(rowIndex+1)]
        T[0] = T[1] = 1
        for row in xrange(1,rowIndex):
        	T[-1] = T[1]
        	T[1] = T[1] + T[0]
        	for i in xrange(2,row+2):
        		T[i] = T[i] + T[-1]
        		T[-1] = 1 if i == rowIndex else T[i] - T[-1]
        		print T
        return T

if __name__ == '__main__':
	print Solution().getRow(4)
	# Solution().getRow(5)