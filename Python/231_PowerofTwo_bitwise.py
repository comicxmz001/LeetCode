class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
        	return False
        return n&(n-1) == 0

for x in xrange(10):
	print "{}: {}".format(x, Solution().isPowerOfTwo(x))
