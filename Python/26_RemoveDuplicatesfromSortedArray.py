class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l= len(nums)
        if l<=1:
        	print nums
        i = 0
        for j in xrange(l-1):
        	if nums[i] == nums[i+1]:
        		nums.remove(nums[i])
        	else:
	        	i += 1
        print nums

n = [1,1,1,2]
Solution().removeDuplicates(n)
