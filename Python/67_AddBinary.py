class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        adigit = 0
        bdigit = 0
        carry = 0
        res = ""
        while la > 0 or lb > 0 or carry == 1:
            adigit = 0
            bdigit = 0
            if la > 0:
                adigit = a[la - 1]
                la -= 1
            if lb > 0:
                bdigit = b[lb - 1]
                lb -= 1
            if carry == 0:
                tmp = int(adigit) + int(bdigit)
            else:
                tmp = int(adigit) + int(bdigit) + carry
            res = str(tmp%2) + res
            carry = 1 if tmp >= 2 else 0
        return res

if __name__ == '__main__':
    a = "1010"
    b = "1000"
    print Solution().addBinary(a, b)
