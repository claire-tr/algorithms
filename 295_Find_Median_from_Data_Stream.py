from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(large, num)
        if len(large) > len(small):
            heappush(small, -heappop(large))
        print small
        print large
        print '-' * 20

    def findMedian(self):
        small, large = self.heaps
        if len(large) < len(small):
            return float(small[0])
        return (large[0] - small[0]) / 2.0


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.addNum(3)
    mf.addNum(4)
    print mf.findMedian()