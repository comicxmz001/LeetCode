# A typical DP problem
# 
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
        	return len(nums)
        T = [1 for x in xrange(len(nums))]

        for i in xrange(1,len(nums)):
        	for j in xrange(i):
        		if nums[j] < nums[i]:
        			T[i] = max(T[i],T[j]+1)
        return max(T)

if __name__ == '__main__':
	arr = [3,4,-1,0,6,2,3]
	arr1 = []
	arr2 = [10,9,2,5,3,7,101,18]
	print Solution().lengthOfLIS(arr2)