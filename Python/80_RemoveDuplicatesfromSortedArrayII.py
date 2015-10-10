class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        j= 0
        for i in xrange(1,len(nums)):
            if nums[j] == nums[i]:  
                count += 1
                if count < 2:
                    j = j+1
                    nums[j] = nums[i]
                    continue
                else: #count == 2
                    continue
            else:
                j = j + 1
                nums[j] = nums[i]
                count = 0
        return j+1



n = [1]
print Solution().removeDuplicates(n)

"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length"""