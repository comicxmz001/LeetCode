class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        op = '+'
        if x[0] == '+' or x[0]== '-':
        	op = x[0]
        	x = x[1:]
    	#reverse
    	res = ""
    	for i in xrange(len(x),0,-1):
    		res += x[i-1]
        return self.checksize(int(op+res))
    def checksize(self,n):
    	if n > 2147483647:
    		return 0
    	if n < -2147483648:
    		return -0
    	return n

n = -1534236469
print Solution().reverse(n)