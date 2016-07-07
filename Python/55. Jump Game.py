class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if 0<= n <= 1:
            return True
            
        maxIndex = 0
        currIndex = 0
        
        while currIndex < n and currIndex <= maxIndex:
            maxIndex = max(currIndex + nums[currIndex], maxIndex)
            currIndex += 1
            if maxIndex >= n-1:
                return True
        
        return False