class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
        #initialize matrix  
        matrix = [[0 for x in range(n)] for x in range(n)] 
        direction ={'LEFT':0,'RIGHT':1, 'DOWN':2, 'UP':3}
        margin = {'left':0,'right':n-1, 'top':0, 'bottom':n-1}
        mSize = n*n

        d = direction['RIGHT'] #direction
        curRow = 0 #row cursor
        curCol = 0 #col cursor
        i=1
        while mSize > 0:
            matrix[curRow][curCol] = i
            i += 1
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
        return  matrix

n = 4
#print matrix
foo = Solution()
print foo.spiralOrder(n)