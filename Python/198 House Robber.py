class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        if len(nums) == 1:
        	return nums[0]
        if len(nums) == 2:
        	return max(nums[0],nums[1])

        T = [nums[0],max(nums[1],nums[0])]
        # You always have two choices, rob or not
        # rob: nums[i] (the one you are robbing) + T[i-2](cannot rob adjacent house)
        # T[i] = max(T[i-1],nums[i]+T[i-2])
        
        for i in xrange(2,len(nums)):
        	T.append(max(T[i-1],nums[i]+T[i-2]))
        return T[-1]

if __name__ == '__main__':
	nums = [2,1,1,2]
	print Solution().rob(nums)