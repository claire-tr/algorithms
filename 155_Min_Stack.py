class MinStack(object):
    # Minimum is a status, need to be updated every time when the stack changes
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.curMin = sys.maxint
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.curMin = min(self.curMin, x)
        self.stack.append([x, self.curMin])

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




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()