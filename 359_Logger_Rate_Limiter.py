class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        '''
        Instead of logging print times, I store the earliest time a message can be printed again.
        Should be slightly faster, because I don't always have to add or subtract (e.g., timestamp < log[message] + 10)
        but only do in the true case. Also, it leads to a shorter/simpler longest line of code.
        '''
        if timestamp < self.timer.get(message, 0):
            # if message not in timer, return 0 as default value
            return False
        self.timer[message] = timestamp + 10
        return True
