# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # search from 0-n
        return self.findBadVersion(0,n) 
        
    def findBadVersion(self, a, b):
        """
        : type a: int
        : type b: int
        : rtype: int
        """
        mid = (a+b)//2
        # in this case, b = a+1, and can only be called if last call of 
        # isBadVersion returns fail. This also means the mid in previous 
        # findBadVersion (previous_mid == this.a) was not a bad version!
        # Thus return b. e.g. n = 7, badversion = 7.
        if a == mid: 
            return b
        else:
            if isBadVersion(mid):
                return self.findBadVersion(a,mid)
            else:
                return self.findBadVersion(mid,b)
            
        