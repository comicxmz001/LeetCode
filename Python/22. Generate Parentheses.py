class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self._generate(n, res, '', 0, 0)
        return res
        
    def _generate(self, n, res, p, left, right):
        if len(p) == n*2:
            res.append(p)
            return
        
        # continue backtracking
        if left < n:
            self._generate(n, res, p + '(', left + 1, right)
        if right < left:
            self._generate(n, res, p + ')', left, right + 1)
        