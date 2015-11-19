class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # use set()
        # check each row
        for i in xrange(9):
            row = set()
            for j in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
        # check each column
        for j in xrange(9):
            column = set()
            for i in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] in column:
                        return False
                    else:
                        column.add(board[i][j])

        # check 3x3 sub boxes, a 9x9 sudoku contains 9 3x3 sub boxes
        for i in xrange(0, 9, 3):  # row
            for j in xrange(0, 9, 3):  # column
                # for subbox[i][j]
                box = set()
                for a in xrange(i, i + 3):
                    for b in xrange(j, j + 3):
                        if board[a][b] != '.':
                            if board[a][b] in box:
                                return False
                            else:
                                box.add(board[a][b])
        return True

if __name__ == '__main__':
    mystr = ["......5..", ".........", ".........", "93..2.4..",
             "..7...3..", ".........", "...34....", ".....3...", ".....52.."]
    print Solution().isValidSudoku(mystr)
