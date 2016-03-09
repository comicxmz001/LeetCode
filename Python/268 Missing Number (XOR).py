class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        
        for i in xrange(len(nums)):
            res ^= nums[i]
            res ^= i
        return res