class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
            return self._sum(a,b)
        else: # different sign
            a,b = max (a,b),min(a,b)
            if a > abs(b):
                return self._substract(a,abs(b))
            else:
                return -self._substract(abs(b), a)


    def _sum(self, a, b):
        while b != 0: # b is used as carry in future loop
            # carry
            carry = a & b
            
            # sum
            a = a ^ b
            
            # leftshif carry and save assign carry to b
            b = carry << 1
        return a

    def _substract(self, a, b):
        while b != 0:
            borrow = (~a) & b

            a = a ^ b

            b = borrow << 1
        return a

if __name__ == '__main__':
    print Solution().getSum(1, -1)