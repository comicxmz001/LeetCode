class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Cycle detection, see turtoise and hare problem 
        #https://upload.wikimedia.org/wikipedia/commons/5/5f/Tortoise_and_hare_algorithm.svg
        #x2 always steps 1+ step than x1. eventually, there will be a situation that x1 == x2, which means a loop is found.
        #Then, if the break point, X_n == 1 (1 is the item we are looking for), then n is a happy number. Otherwise, return false.
        x1 = n
        x2 = self.digitSquareSum(n)
        while x1 != x2:
        	x1 = self.digitSquareSum(x1)
        	x2 = self.digitSquareSum(self.digitSquareSum(x2))
    	return x1 == 1 # x2 is ok, since when the while loop is broken, x1 == x2

    #calculate the square sum of each digit
    def digitSquareSum(self, n):
    	res = 0
    	while n:
    		tmp = n % 10
    		res += tmp**2
    		n = int(n)/10
    	return res

n = 19
foo = Solution()
print foo.isHappy(n)