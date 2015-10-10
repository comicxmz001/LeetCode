class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in xrange(len(nums)):
        	if nums[index] == val:
        		del nums[index]
        	else:
	        	index += 1
    	return len(nums)

nums = [1,2,2,3]
val = 2
foo = Solution()
print foo.removeElement(nums,val)