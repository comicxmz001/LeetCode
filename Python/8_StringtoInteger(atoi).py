import sys
# Has to filter spaces,operator and other letters
# Also has to check if the number exceed sys.maxint and -sys.maxint-1 (equivalent to minint)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
        	return 0
        opcount = 0
        hasdigit = 0
        res =""
        for i in xrange(len(str)):
        	c = str[i]
        	#print "str is",res
        	#filter space
        	if c == ' ':
        		if hasdigit == 1:
	        		return self.checksize(int(res))
	        	if opcount == 1:
	        		return 0
	        elif c == '+' or c== '-':
	        	if opcount == 1:
	        		return 0
	        	else:
	        		res += c
	        		opcount = 1
	        #is digit
	        elif 47<ord(c)<58:
	        	res += c
	        	hasdigit = 1
	        else: #other characters
	        	if hasdigit ==1:
	        		return self.checksize(int(res))
	        	return 0
    	
        return self.checksize(int(res))
    def checksize(self,n):
    	if n > 2147483647:
    		return 2147483647
    	if n < -2147483648:
    		return -2147483648
    	return n


str = "      -11919730356x"
print Solution().myAtoi(str)
#print ord('9')
print -11919730356 < -2147483648