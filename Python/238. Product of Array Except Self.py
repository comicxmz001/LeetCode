class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [0 for x in xrange(len(nums))]
        res[0] = 1 

        # split it into three parts: L, res[i], R
        # calculate L
        for i in xrange(1,len(nums)) :
            res[i] = res[i-1]*nums[i-1]
        # calculate R
        r = 1
        for i in xrange(len(nums),0,-1):
            res[i-1] *= r # the last element has no right elements, so r = 1
            r *= nums[i-1]
        return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    print Solution().productExceptSelf(nums)