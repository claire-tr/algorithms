import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_t = collections.Counter(t) # don't care about the index, just the frequency
        dic_s = collections.defaultdict(list) # index matters
        window = []
        res = ''

        for i, c in filter(lambda x: x[1] in t, enumerate(s)):
            # Only care about characters that are in t
            dic_s[c].append(i)
            window.append(i)

            if len(dic_s[c]) > dic_t[c]:
                window.remove(dic_s[c].pop(0))

            if len(window) == len(t) and (res == '' or window[-1] - window[0] < len(res)):
                res = s[window[0]:window[-1] + 1]

        return res