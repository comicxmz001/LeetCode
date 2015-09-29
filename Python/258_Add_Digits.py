class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <10:
        	return num
        while num >= 10:
	       	foo = str(num)
	        result = 0
	        for digit in foo:
	        	result += int(digit)
	        num = result
	    return num

#Test code 
boo = Solution()
boo.addDigits(38)