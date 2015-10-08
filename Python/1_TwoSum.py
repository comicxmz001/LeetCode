class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hash table
        n = {}
        #hash all the nums into a hash table
        for i in xrange(len(nums)):
        	n[nums[i]] = i
        # target - nums[i] should be an existing key in n{}
        # Also, since index1 < index2, self add is not allowed!
        for index1 in xrange(len(nums)):
        	tmp = target - nums[index1]
        	if tmp in n and n[tmp] > index1:
        		return [index1+1,n[tmp]+1]

nums = [3,2,4]
target = 6
foo = Solution()
print foo.twoSum(nums,target)