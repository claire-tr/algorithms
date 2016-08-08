#coding=utf-8
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        '''
        这题与算法无关，是个数学题。思想是把所有需要相加的值存在第一个数，然后把这个范围的最后一位的下一位减去这个inc,
        这样我所以这个范围在求最终值的时候，都可以加上这个inc，而后面的数就不会加上inc。
        '''
        res = [0] * length
        for update in updates:
            res[update[0]] += update[2]
            if update[1] < length - 1:
                res[update[1] + 1] += - update[2]
        for i in xrange(1, length):
            res[i] += res[i-1]
        return res
