class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.__queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        p = self.__queue[-1]
        tmpQ = self.__queue[:-1]
        self.__queue = tmpQ
        return p
        

    def top(self):
        """
        :rtype: int
        """
        return self.__queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.__queue

    # This method is not requred, just for helping test the code
    def printstack(self):
        print self.__queue


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(9)
    stack.pop()
    stack.pop()
    stack.printstack()
    print stack.empty()



