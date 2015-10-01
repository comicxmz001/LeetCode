class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        row = len(matrix)
        if row == 0:
            return matrix
        if row == 1:
            result = matrix[0]
            return result
        col = len(matrix[0])
        direction ={'LEFT':0,'RIGHT':1, 'DOWN':2, 'UP':3}
        margin = {'left':0,'right':col-1, 'top':0, 'bottom':row-1}
        mSize = row*col

        d = direction['RIGHT'] #direction
        curRow = 0 #row cursor
        curCol = 0 #col cursor
        while mSize > 0:
            result.append(matrix[curRow][curCol])
            mSize -=1
            if d == direction['RIGHT']:
                if curCol == margin['right']:
                    d = direction['DOWN']
                    margin['top'] +=1
                    curRow += 1
                    continue
                curCol +=1
                continue
            if d == direction['LEFT']:
                if curCol == margin['left']:
                    d = direction['UP']
                    margin['bottom'] -= 1
                    curRow -=1
                    continue
                curCol -=1
                continue
            if d == direction['DOWN']:
                if curRow == margin['bottom']:
                    d = direction['LEFT']
                    margin['right'] -= 1
                    curCol -= 1
                    continue
                curRow +=1
                continue
            if d == direction['UP']:
                if curRow == margin['top']:
                    d = direction['RIGHT']
                    margin['left'] += 1
                    curCol += 1
                    continue
                curRow -=1
                continue
        return  result

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#print matrix
foo = Solution()
print foo.spiralOrder(matrix)