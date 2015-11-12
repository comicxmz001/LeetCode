class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(k):
        	nums.insert(0,nums.pop())


if __name__ == '__main__':
	nums = [-1,2,3,4,5]
	k = 3
	Solution().rotate(nums,k)
	print nums