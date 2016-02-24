class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
            
        ranges = []
        start = nums[0]
        end = nums[0]
        for i in xrange(1,len(nums)):
            if nums[i] - end == 1:
                end = nums[i]
                continue
            else:
                if start==end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                start = nums[i]
                end = nums[i]
                
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))
        return ranges
            