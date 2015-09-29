class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        index = 0
        for i in xrange(length):
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
                continue
            index += 1
                

            
#Test code
foo = Solution()
a1 = [2,0,0,0,0,0,0,0,0,0,3,0,5,60,0,1]
foo.moveZeroes(a1)
print a1