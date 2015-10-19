class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
        	return False
        if len(matrix[0]) == 0:
        	return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
        	if matrix[row][col] < target:
        		row += 1
        	elif matrix[row][col] > target:
        		col -= 1
        	else:
        		return True
        return False


n = 51
m = [[1, 3, 5, 7], 
	[10, 11, 16, 20], 
	[23, 30, 34, 50]]

print Solution().searchMatrix(m,n)