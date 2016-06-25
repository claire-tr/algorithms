class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.nums = []


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        if len(self.nums) == 0:
            return 0
        elif len(self.nums) < 3:
            return float(sum(self.nums))/len(self.nums)
        else:
            return float(sum(self.nums[-3:]))/3
