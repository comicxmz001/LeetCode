class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._s = []
        self.t = len(self._s)-1
        self.curMin = 2147483647
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.curMin = x if x < self.curMin else self.curMin
        if self.t < len(self._s)-1 and len(self._s)>0:
            self._s[self.t+1] = [x,self.curMin]
        else:
            self._s.append([x,self.curMin])
        self.t += 1

    def pop(self):
        """
        :rtype: nothing
        """
        p = self._s[self.t][0]
        self.t -= 1
        self.curMin = 2147483647 if self.t == -1 else self._s[self.t][1]
        # print "t=",self.t,"self.curMin=",self.curMin
        return p
        

    def top(self):
        """
        :rtype: int
        """
        return self._s[self.t][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._s[self.t][1]

    def getStack(self):
        return self._s[:self.t+1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(2147483646)
    stack.push(2147483645)
    stack.push(2147483647)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push(2147483647)
    stack.push(-2147483648)
    stack.pop()
    print stack.getMin()



