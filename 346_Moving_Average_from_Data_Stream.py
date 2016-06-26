class MovingAverage(object):
    # Use fixed size deque
    # https://leetcode.com/discuss/100373/4-line-python-solution-using-deque
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)