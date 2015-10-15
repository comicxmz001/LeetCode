class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
        	return False
        while n/2>0:
        	a = float(n/2)
        	b = float(n)/2.0
        	if a != b:
        		return False
        	n = n/2
        return True

for x in xrange(10):
	print "{}: {}".format(x, Solution().isPowerOfTwo(x))