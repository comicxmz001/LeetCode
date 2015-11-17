class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0:
            return None
        self.m = [[0 for x in xrange(len(matrix[0])+1)] for x in xrange(len(matrix)+1)]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                self.m[i+1][j+1] = self.m[i][j+1] + self.m[i+1][j] - self.m[i][j] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.m[row2+1][col2+1] - self.m[row2+1][col1] - self.m[row1][col2+1] + self.m[row1][col1]
        

if __name__ == '__main__':
    matrix =  [
                [3, 0, 1, 4, 2],
                [5, 6, 3, 2, 1],
                [1, 2, 0, 1, 5],
                [4, 1, 0, 1, 7],
                [1, 0, 3, 0, 5]
             ]
    m2 = [] 
    numMatrix = NumMatrix(matrix)
    print numMatrix.sumRegion(1, 1, 2, 2)
    print numMatrix.sumRegion(2, 1, 4, 3)
    print numMatrix.sumRegion(1, 2, 2, 4)