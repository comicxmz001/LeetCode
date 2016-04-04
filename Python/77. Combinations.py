class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        self.backtrack(res,[],1,n,k)
        return res
        
    def backtrack(self,res, path, index, n, k):
        if k == 0: # end of path
            res.append(list(path))
            return 
        for i in xrange(index,n+1):
            path.append(i)
            self.backtrack(res, path, i+1, n, k-1)
            path.pop()


if __name__ == "__main__":
    print Solution().combine(4,2)