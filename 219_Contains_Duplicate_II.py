from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = defaultdict(list)
        for i in xrange(len(nums)):
            dic[nums[i]].append(i)
        for key, value in dic.iteritems():
            for i in range(1, len(value)):
                if value[i] - value[i-1] <= k:
                    return True
        return False
