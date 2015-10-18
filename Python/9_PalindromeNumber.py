class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x< 0 or (x!= 0 and x%10 == 0): #when reversed, at least 10 time small than original. e.g. 10 => 1, 100 => 1
        	return False
        rev = 0

        #Only do half
        while x > rev:
        	rev = rev*10 + x%10
        	x /= 10

        # x == rev (lenth is even) e.g. 2222
        # x == rev/10 (lenth is odd) e.g. 222
        # if any of the condition is True, then this number is palindrome
        # For example, 12321
        # 			1: x = 1232, 	rev = 1
        #			2: x = 123,		rev = 12
        #			3: x = 12,		rev = 123
        #			4: break, as x < rev
        #			5: return True, as x = rev/10 (int type)
        return x == rev or x == rev/10


n = 0
print Solution().isPalindrome(n)