class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        return len(set(zip(pattern,str))) == len(set(pattern)) == len(set(str)) and len(pattern)== len(str)

mypattern = "abba"
mystr = "hat bat hat bat"
print Solution().wordPattern(mypattern,mystr)