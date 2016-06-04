class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # min, as you cannot slant the container
            h = min(height[left], height[right])
            # calculate area
            area = max(area, (right - left) * h)
            # move the pointers
            # while moving the pointer, the width (right-left) is always decreasing, 
            # only a longer height would propable lead to a larger area (width*height)
            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
        return area
            