class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
        	return False
        if num == 1:
        	return True
        factors = [2,3,5]
        for factor in factors:
        	while num%factor == 0:
        		num /= factor
        return True if num==1 else False

if __name__ == "__main__":
	print Solution().isUgly(14)