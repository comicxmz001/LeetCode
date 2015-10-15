class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1] += 1
        if digits[len(digits)-1] < 10:
        	return digits
        for i in xrange(len(digits)-1,0,-1):
        	if digits[i] == 10:
        		digits[i] = 0
        		digits[i-1] += 1
        	else:
        		break
        if digits[0] == 10:
        	digits[0] = 0
        	digits = [1] + digits
        return digits

digits = [0,9,7,9]
print Solution().plusOne(digits)
