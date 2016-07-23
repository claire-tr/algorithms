import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        '''
            Frequency is in range(len(nums))
            Use the idea of the bucket sort,
            Build a array of list to be buckets with length 1 to sort.
            First scan the array, store the frequency for each elements in a hash map.
            Then scan the hash map, put the key-value pair in corresponding bucket
            add the first k element in the bucket to the result

        '''
        bucket = [[] for _ in nums]
        cnt = collections.defaultdict(int)
        res = []
        
        for n in nums:
            cnt[n] += 1
        for n, f in cnt.iteritems():
            bucket[len(nums) - f].append(n)
        
        for i in xrange(0, len(nums)):
            if len(res) >= k:
                break
            if bucket[i]:
                res += bucket[i].pop(0)
        return res