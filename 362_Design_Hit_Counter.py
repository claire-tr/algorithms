#coding=utf-8
class HitCounter(object):
    '''
        适合getHits调用的多的情况,每次getHits直接返回一个值即可
        存(timestamp, #hits),每秒只占用一个空间,fixed size,避免每秒里面hit过多造成空间占用太多
        在hit和getHits里面都要做remove,避免100000次hit,一次getHits,导致空间太多
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_of_hits = 0
        self.time_hits = collections.deque()


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        while self.time_hits and self.time_hits[0][0] < timestamp - 300:
            self.num_of_hits -= self.time_hits.popleft()[1]

        if not self.time_hits or self.time_hits[-1][0] != timestamp:
            self.time_hits.append([timestamp, 1])
        else:
            self.time_hits[-1][1] += 1

        self.num_of_hits += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.time_hits and self.time_hits[0][0] <= timestamp - 300:
            self.num_of_hits -= self.time_hits.popleft()[1]

        return self.num_of_hits


    '''
        fixed size
        适合于getHits调用得少的情况,因为getHits要遍历整个数组

        O(s) s is total seconds in given time interval, in this case 300.
        basic ideal is using buckets.
        1 bucket for every second because we only need to keep the recent hits info for 300 seconds.
        hit[] array is wrapped around by mod operation.
        Each hit bucket is associated with times[] bucket which record current time.
        If it is not current time, it means it is 300s or 600s... ago and need to reset to 1.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [i for i in range(1, 301)]
        self.hit = [0] * 300

    def hit(self, timestamp):
        index = timestamp % 300
        if self.time[index] != timestamp:
            self.hit[index] = 1
            self.time[index] = timestamp
        else:
            self.hit[index] += 1
        return

    def getHits(self, timestamp):

        total = 0
        for i in xrange(300):
            if timestamp - self.time[i] < 300:
                total += self.hit[i]
        return total
            '''