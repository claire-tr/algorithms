class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for s in strs:
            s_s = str(sorted(s))
            res[s_s].append(s)
        return res.values()

