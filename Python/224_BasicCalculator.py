class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
        	return 0

        # the string is actually converted to [+num1,-num2,-num3...]
        # so, you should always get the sign before the number.
        # There is a trap with negative operation, since int()/int() will round down, e.g. 2/3 = 1, 
        # when dealing with negatevie, -2/3 = round.down(-2/3) = round.down(-0.333) = -1. This will result in wrong restul.
        # Thus, simple change tmp to -tmp, and then change back after the operation.

        num = 0
        sign = "+" #be default, the first num has to be added to the stack
        stack = []
        for i in xrange(len(s)):
        	# calculate num
        	if s[i].isdigit():
        		num = num*10 + int(s[i])
        	# calculate sign
        	if (not s[i].isdigit() and not s[i].isspace()) or (i == len(s) -1):
        		# still using the previous sign
        		if sign == "+":
        			stack.append(num)
        		elif sign == "-":
        			stack.append(-num)
        		elif sign == "*":
        			stack.append(stack.pop()*num)
        		else: # /
        			tmp = stack.pop ()
        			if tmp < 0:
	        			stack.append(-(tmp/-num))
	        		else:
	        			stack.append(tmp/num)
        		num = 0
        		sign = s[i] # update to new sign.
    	return sum(stack)


if __name__ == '__main__':
	exp = "3 - 2/3 + 3 - 2 + 3*2" # 7
	exp2 =  "3+5 / 2 "
	print Solution().calculate(exp2)