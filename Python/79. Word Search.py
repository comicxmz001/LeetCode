class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # check if the word is valid
        if not word: return True
        
        # check if the board is valid
        if not board: return False
        if not board[0]: return False
        
        # track the board
        visited = [[False for i in xrange(len(board[0]))] for _ in xrange(len(board))]
        
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if self.search(board, word, visited, row, col):
                    return True
        return False
    
    def search(self, board, word, visited, row, col):
        # if already find all characters
        if not word: return True
        
        # if current pos is not on the board, returnf False
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        # if the char does not matche the word[0] or this point has been visited,
        # return False
        if board[row][col] != word[0] or visited[row][col]:
            return False
        
        # mark the pos as visited
        visited[row][col] = True
        
        # backtrack, four directions
        if (self.search(board, word[1:], visited, row - 1, col) or
            self.search(board, word[1:], visited, row + 1, col) or
            self.search(board, word[1:], visited, row, col - 1) or
            self.search(board, word[1:], visited, row, col + 1) ):
                return True
        
        
        # resume previous status
        visited[row][col] = False
        
        return False