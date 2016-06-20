from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hash Table
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        for key, value in table.iteritems():
            if value == 1:
                return key


        # # XOR
        # res = 0
        # for n in nums:
        #     res = res ^ n
        # return res