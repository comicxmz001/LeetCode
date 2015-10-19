class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
        	return False
        if len(set(zip(pattern,str))) != len (set(str)):
        	return False
        if len(set(zip(pattern,str))) != len(set(pattern)):
        	return False
        return True

mypattern = "abba"
mystr = "hat bat hat bat"
print Solution().wordPattern(mypattern,mystr)