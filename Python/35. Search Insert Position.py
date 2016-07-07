class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        O(logn)
        """
        low = 0
        high = len(nums) - 1
        if target <= nums[low]:
        	return low
        if target > nums[high]:
        	return high+1
        while low < high:
        	mid = (low + high) // 2
        	# print low, high, mid
        	if nums[mid] < target <= nums[mid+1]:
        		return mid+1
        	if nums[mid] >= target:
        		high = mid
        	else:
        		low = mid

    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        60ms O(n)
        """
        index = 0
        for num in nums:
        	if num < target:
        		index += 1
        return index 

if __name__ == '__main__':
	target = 7
	nums = [1,3,5,6]
	# nums = [1]
	print Solution().searchInsert(nums,target)