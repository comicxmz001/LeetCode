class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1],[1,1]]
        if numRows == 0:
        	return []
        elif numRows == 1:
        	return [[1]]
        else:
	        old = [1,1]
        	for i in xrange(numRows-2):
	        	temp = [1]
	        	for j in xrange(len(old)-1):
	        		temp.append(old[j]+old[j+1])
	        	temp.append(1)
	        	res.append(temp)
	        	old = temp
        	return res

if __name__ == '__main__':
	print Solution().generate(6)
	
