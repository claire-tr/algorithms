class MinStack(object):
    # Minimum is a status, need to be updated every time when the stack changes
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin =self.getMin()
        self.stack.append([x, min(curMin, x)])

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.curMin = self.stack.pop()[1]

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        else:
            return sys.maxint

