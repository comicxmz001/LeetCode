class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return 0
    	romanNum = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' :1000}
        #Left is always larger than right, so if left < right, means right-left, 
        #e.g. IV = V -I
        # III can only appear at the end of string
        # Only single I can be placed before other letters.
        arr = [romanNum[x] for x in s]
        res = sum(arr)
        for i in xrange(len(arr)-1):
        	# arr[i]+arr[i+1] => arr[i+1] - arr[i]
        	#Thus, should take 2*arr[i] from the old res.
        	if arr[i] < arr [i+1]: 
        		res -= 2* arr[i]
        return res

RM = "DCXXI"
print Solution().romanToInt(RM)