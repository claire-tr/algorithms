class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        res, start = 0, 0
        dic = collections.defaultdict(int)

        for i in xrange(len(s)):
            dic[s[i]] += 1
            while len(dic) > k:
                dic[s[start]] -= 1
                if dic[s[start]] == 0:
                    dic.pop(s[start])
                start += 1
            res = max(res, i - start + 1)
        return res